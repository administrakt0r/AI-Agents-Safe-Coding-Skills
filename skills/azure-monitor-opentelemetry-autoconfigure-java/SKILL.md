---
name: azure-monitor-opentelemetry-autoconfigure-java
description: Azure Monitor OpenTelemetry Autoconfigure for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights with automatic configuration.
risk: safe
source: community
date_added: '2026-04-03'
---

# Azure Monitor OpenTelemetry Autoconfigure for Java

Export OpenTelemetry telemetry data to Azure Monitor / Application Insights using the recommended autoconfigure approach, providing automatic instrumentation of common libraries, simplified configuration, and better integration with the OpenTelemetry SDK.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-monitor-opentelemetry-autoconfigure</artifactId>
    <version>1.0.0-beta.x</version> <!-- Use the latest version -->
</dependency>
```

## Environment Variables

```bash
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=xxx;IngestionEndpoint=https://xxx.in.applicationinsights.azure.com/
```

## Basic Setup

### Using Environment Variable

```java
import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;
import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdkBuilder;
import io.opentelemetry.api.OpenTelemetry;
import com.azure.monitor.opentelemetry.exporter.AzureMonitorExporter;

// Connection string is automatically picked up from APPLICATIONINSIGHTS_CONNECTION_STRING env var
AutoConfiguredOpenTelemetrySdkBuilder sdkBuilder = AutoConfiguredOpenTelemetrySdk.builder();
AzureMonitorExporter.customize(sdkBuilder);
OpenTelemetry openTelemetry = sdkBuilder.build().getOpenTelemetrySdk();
```

### With Explicit Connection String

```java
AutoConfiguredOpenTelemetrySdkBuilder sdkBuilder = AutoConfiguredOpenTelemetrySdk.builder();
AzureMonitorExporter.customize(sdkBuilder, "{connection-string}");
OpenTelemetry openTelemetry = sdkBuilder.build().getOpenTelemetrySdk();
```

## Creating Spans

```java
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.context.Scope;

// Get tracer
Tracer tracer = openTelemetry.getTracer("com.example.myapp");

// Create span
Span span = tracer.spanBuilder("myOperation").startSpan();

try (Scope scope = span.makeCurrent()) {
    // Your application logic
    doWork();
} catch (Throwable t) {
    span.recordException(t);
    throw t;
} finally {
    span.end();
}
```

## Adding Span Attributes

```java
import io.opentelemetry.api.common.AttributeKey;
import io.opentelemetry.api.common.Attributes;

Span span = tracer.spanBuilder("processOrder")
    .setAttribute("order.id", "12345")
    .setAttribute("customer.tier", "premium")
    .startSpan();

try (Scope scope = span.makeCurrent()) {
    // Add attributes during execution
    span.setAttribute("items.count", 3);
    span.setAttribute("total.amount", 99.99);
    
    processOrder();
} finally {
    span.end();
}
```

## Custom Span Processor

```java
import io.opentelemetry.sdk.trace.SpanProcessor;
import io.opentelemetry.sdk.trace.ReadWriteSpan;
import io.opentelemetry.sdk.trace.ReadableSpan;
import io.opentelemetry.context.Context;

private static final AttributeKey<String> CUSTOM_ATTR = AttributeKey.stringKey("custom.attribute");

SpanProcessor customProcessor = new SpanProcessor() {
    @Override
    public void onStart(Context context, ReadWriteSpan span) {
        // Add custom attribute to every span
        span.setAttribute(CUSTOM_ATTR, "customValue");
    }

    @Override
    public boolean isStartRequired() {
        return true;
    }

    @Override
    public void onEnd(ReadableSpan span) {
        // Post-processing if needed
    }

    @Override
    public boolean isEndRequired() {
        return false;
    }
};

// Register processor
AutoConfiguredOpenTelemetrySdkBuilder sdkBuilder = AutoConfiguredOpenTelemetrySdk.builder();
AzureMonitorExporter.customize(sdkBuilder);

sdkBuilder.addTracerProviderCustomizer(
    (sdkTracerProviderBuilder, configProperties) -> 
        sdkTracerProviderBuilder.addSpanProcessor(customProcessor)
);

OpenTelemetry openTelemetry = sdkBuilder.build().getOpenTelemetrySdk();
```

## Nested Spans

```java
public void parentOperation() {
    Span parentSpan = tracer.spanBuilder("parentOperation").startSpan();
    try (Scope scope = parentSpan.makeCurrent()) {
        childOperation();
    } finally {
        parentSpan.end();
    }
}

public void childOperation() {
    // Automatically links to parent via Context
    Span childSpan = tracer.spanBuilder("childOperation").startSpan();
    try (Scope scope = childSpan.makeCurrent()) {
        // Child work
    } finally {
        childSpan.end();
    }
}
```

## Recording Exceptions

```java
Span span = tracer.spanBuilder("riskyOperation").startSpan();
try (Scope scope = span.makeCurrent()) {
    performRiskyWork();
} catch (Exception e) {
    span.recordException(e);
    span.setStatus(io.opentelemetry.api.trace.StatusCode.ERROR, e.getMessage());
    throw e;
} finally {
    span.end();
}
```

## Metrics (via OpenTelemetry)

```java
import io.opentelemetry.api.metrics.Meter;
import io.opentelemetry.api.metrics.LongCounter;
import io.opentelemetry.api.metrics.LongHistogram;

Meter meter = openTelemetry.getMeter("com.example.myapp");

// Counter
LongCounter requestCounter = meter.counterBuilder("http.requests")
    .setDescription("Total HTTP requests")
    .setUnit("requests")
    .build();

requestCounter.add(1, Attributes.of(
    AttributeKey.stringKey("http.method"), "GET",
    AttributeKey.longKey("http.status_code"), 200L
));

// Histogram
LongHistogram latencyHistogram = meter.histogramBuilder("http.latency")
    .setDescription("Request latency")
    .setUnit("ms")
    .ofLongs()
    .build();

latencyHistogram.record(150, Attributes.of(
    AttributeKey.stringKey("http.route"), "/api/users"
));
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| Connection String | Application Insights connection string with instrumentation key |
| Tracer | Creates spans for distributed tracing |
| Span | Represents a unit of work with timing and attributes |
| SpanProcessor | Intercepts span lifecycle for customization |
| Autoconfigure | Automatically configures the OpenTelemetry SDK with Azure Monitor integration |

## Best Practices

1. **Use autoconfigure** — Ensure you are using `azure-monitor-opentelemetry-autoconfigure` instead of the deprecated `azure-monitor-opentelemetry-exporter` package.
2. **Set meaningful span names** — Use descriptive operation names
3. **Add relevant attributes** — Include contextual data for debugging
4. **Handle exceptions** — Always record exceptions on spans
5. **Use semantic conventions** — Follow OpenTelemetry semantic conventions
6. **End spans in finally** — Ensure spans are always ended
7. **Use try-with-resources** — Scope management with try-with-resources pattern

## Reference Links

| Resource | URL |
|----------|-----|
| Maven Package | https://central.sonatype.com/artifact/com.azure/azure-monitor-opentelemetry-autoconfigure |
| OpenTelemetry Java | https://opentelemetry.io/docs/languages/java/ |
| Application Insights | https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
