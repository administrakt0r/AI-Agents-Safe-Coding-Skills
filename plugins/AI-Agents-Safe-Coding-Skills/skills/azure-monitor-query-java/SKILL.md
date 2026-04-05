---
name: azure-monitor-query-java
description: Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Monitor Query SDK for Java

Client libraries for querying Azure Monitor Logs and Metrics using the new, modular `azure-monitor-query-logs` and `azure-monitor-query-metrics` SDKs.

## Installation

Add the corresponding packages to your `pom.xml` depending on your needs.

**For Logs:**

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-monitor-query-logs</artifactId>
    <version>1.x.x</version> <!-- Use the latest version -->
</dependency>
```

**For Metrics:**

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-monitor-query-metrics</artifactId>
    <version>1.x.x</version> <!-- Use the latest version -->
</dependency>
```

Or use the Azure SDK BOM for version management:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.azure</groupId>
            <artifactId>azure-sdk-bom</artifactId>
            <version>{bom_version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>com.azure</groupId>
        <artifactId>azure-monitor-query-logs</artifactId>
    </dependency>
    <dependency>
        <groupId>com.azure</groupId>
        <artifactId>azure-monitor-query-metrics</artifactId>
    </dependency>
</dependencies>
```

## Prerequisites

- Log Analytics workspace (for logs queries)
- Azure resource (for metrics queries)
- TokenCredential with appropriate permissions

## Environment Variables

```bash
LOG_ANALYTICS_WORKSPACE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_RESOURCE_ID=/subscriptions/{sub}/resourceGroups/{rg}/providers/{provider}/{resource}
```

## Client Creation

### LogsQueryClient (Sync)

```java
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.azure.monitor.query.logs.LogsQueryClient;
import com.azure.monitor.query.logs.LogsQueryClientBuilder;
import com.azure.core.credential.TokenCredential;

TokenCredential credential = new DefaultAzureCredentialBuilder().build();

LogsQueryClient logsClient = new LogsQueryClientBuilder()
    .credential(credential)
    .buildClient();
```

### LogsQueryAsyncClient

```java
import com.azure.monitor.query.logs.LogsQueryAsyncClient;

LogsQueryAsyncClient logsAsyncClient = new LogsQueryClientBuilder()
    .credential(credential)
    .buildAsyncClient();
```

### MetricsQueryClient (Sync)

```java
import com.azure.monitor.query.metrics.MetricsQueryClient;
import com.azure.monitor.query.metrics.MetricsQueryClientBuilder;

MetricsQueryClient metricsClient = new MetricsQueryClientBuilder()
    .credential(credential)
    .buildClient();
```

### MetricsQueryAsyncClient

```java
import com.azure.monitor.query.metrics.MetricsQueryAsyncClient;

MetricsQueryAsyncClient metricsAsyncClient = new MetricsQueryClientBuilder()
    .credential(credential)
    .buildAsyncClient();
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| Logs | Log and performance data from Azure resources via Kusto Query Language |
| Metrics | Numeric time-series data collected at regular intervals |
| Workspace ID | Log Analytics workspace identifier |
| Resource ID | Azure resource URI for metrics queries |
| LogsQueryTimeInterval | Time range for the log query |

## Logs Query Operations

### Basic Query

```java
import com.azure.monitor.query.logs.models.LogsQueryResult;
import com.azure.monitor.query.logs.models.LogsTableRow;
import com.azure.monitor.query.logs.models.LogsQueryTimeInterval;
import java.time.Duration;

LogsQueryResult result = logsClient.queryWorkspace(
    "{workspace-id}",
    "AzureActivity | summarize count() by ResourceGroup | top 10 by count_",
    new LogsQueryTimeInterval(Duration.ofDays(7))
);

for (LogsTableRow row : result.getTable().getRows()) {
    System.out.println(row.getColumnValue("ResourceGroup").get().getValueAsString() + ": " + row.getColumnValue("count_").get().getValueAsString());
}
```

### Query by Resource ID

```java
LogsQueryResult result = logsClient.queryResource(
    "{resource-id}",
    "AzureMetrics | where TimeGenerated > ago(1h)",
    new LogsQueryTimeInterval(Duration.ofDays(1))
);

for (LogsTableRow row : result.getTable().getRows()) {
    System.out.println(row.getColumnValue("MetricName").get().getValueAsString() + " " + row.getColumnValue("Average").get().getValueAsString());
}
```

### Batch Query

```java
import com.azure.monitor.query.logs.models.LogsBatchQuery;
import com.azure.monitor.query.logs.models.LogsBatchQueryResult;
import com.azure.monitor.query.logs.models.LogsBatchQueryResultCollection;
import com.azure.monitor.query.logs.models.LogsQueryResultStatus;
import com.azure.core.util.Context;

LogsBatchQuery batchQuery = new LogsBatchQuery();
String q1 = batchQuery.addWorkspaceQuery("{workspace-id}", "AzureActivity | count", new LogsQueryTimeInterval(Duration.ofDays(1)));
String q2 = batchQuery.addWorkspaceQuery("{workspace-id}", "Heartbeat | count", new LogsQueryTimeInterval(Duration.ofDays(1)));
String q3 = batchQuery.addWorkspaceQuery("{workspace-id}", "Perf | count", new LogsQueryTimeInterval(Duration.ofDays(1)));

LogsBatchQueryResultCollection results = logsClient
    .queryBatchWithResponse(batchQuery, Context.NONE)
    .getValue();

LogsBatchQueryResult result1 = results.getResult(q1);
LogsBatchQueryResult result2 = results.getResult(q2);
LogsBatchQueryResult result3 = results.getResult(q3);

// Check for failures
if (result3.getQueryResultStatus() == LogsQueryResultStatus.FAILURE) {
    System.err.println("Query failed: " + result3.getError().getMessage());
}
```

## Metrics Query Operations

### Basic Metrics Query

```java
import com.azure.monitor.query.metrics.models.MetricsQueryResult;
import com.azure.monitor.query.metrics.models.MetricResult;
import com.azure.monitor.query.metrics.models.TimeSeriesElement;
import com.azure.monitor.query.metrics.models.MetricValue;
import java.util.Arrays;

MetricsQueryResult result = metricsClient.queryResource(
    "{resource-uri}",
    Arrays.asList("SuccessfulCalls", "TotalCalls")
);

for (MetricResult metric : result.getMetrics()) {
    System.out.println("Metric: " + metric.getMetricName());
    for (TimeSeriesElement ts : metric.getTimeSeries()) {
        System.out.println("  Dimensions: " + ts.getMetadata());
        for (MetricValue value : ts.getValues()) {
            System.out.println("    " + value.getTimeStamp() + ": " + value.getTotal());
        }
    }
}
```

### Metrics with Aggregations

```java
import com.azure.monitor.query.metrics.models.MetricsQueryOptions;
import com.azure.monitor.query.metrics.models.AggregationType;
import com.azure.core.http.rest.Response;
import com.azure.core.util.Context;

Response<MetricsQueryResult> response = metricsClient.queryResourceWithResponse(
    "{resource-id}",
    Arrays.asList("SuccessfulCalls", "TotalCalls"),
    new MetricsQueryOptions()
        .setGranularity(Duration.ofHours(1))
        .setAggregations(Arrays.asList(AggregationType.AVERAGE, AggregationType.COUNT)),
    Context.NONE
);

MetricsQueryResult result = response.getValue();
```

## Migration Notes from azure-monitor-query

The legacy combined package `azure-monitor-query` is deprecated. Code must be updated to use the modular packages `azure-monitor-query-logs` and `azure-monitor-query-metrics`.

Key changes:
1. Package imports changed: `com.azure.monitor.query` -> `com.azure.monitor.query.logs` and `com.azure.monitor.query.metrics`
2. `QueryTimeInterval` has been renamed to `LogsQueryTimeInterval` for the logs package, and similarly separated for the metrics package if applicable.
3. Replace the `azure-monitor-query` Maven dependency with `azure-monitor-query-logs` and/or `azure-monitor-query-metrics`.

## Error Handling

```java
import com.azure.core.exception.HttpResponseException;
import com.azure.monitor.query.logs.models.LogsQueryResultStatus;

try {
    LogsQueryResult result = logsClient.queryWorkspace(workspaceId, query, timeInterval);
    
    // Check partial failure
    if (result.getQueryResultStatus() == LogsQueryResultStatus.PARTIAL_FAILURE) {
        System.err.println("Partial failure: " + result.getError().getMessage());
    }
} catch (HttpResponseException e) {
    System.err.println("Query failed: " + e.getMessage());
    System.err.println("Status: " + e.getResponse().getStatusCode());
}
```

## Best Practices

1. **Use batch queries** — Combine multiple queries into a single request
2. **Set appropriate timeouts** — Long queries may need extended server timeout
3. **Limit result size** — Use `top` or `take` in Kusto queries
4. **Use projections** — Select only needed columns with `project`
5. **Check query status** — Handle PARTIAL_FAILURE results gracefully
6. **Cache results** — Metrics don't change frequently; cache when appropriate

## Reference Links

| Resource | URL |
|----------|-----|
| Logs Package | https://central.sonatype.com/artifact/com.azure/azure-monitor-query-logs |
| Metrics Package | https://central.sonatype.com/artifact/com.azure/azure-monitor-query-metrics |
| Migration Guide | https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/monitor/azure-monitor-query-logs/migration-guide.md |
| Kusto Query Language | https://learn.microsoft.com/azure/data-explorer/kusto/query/ |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
