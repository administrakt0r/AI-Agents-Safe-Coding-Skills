content = open('.github/workflows/auto-merge.yml').read()
content = content.replace("headSha = pr.data.head.sha || context.payload.check_suite.head_sha;\n              if (!headSha) {\n                core.setOutput('skip', 'true');\n                return;\n              }", "headSha = pr.data.head.sha;\n              if (!headSha) {\n                headSha = context.payload.check_suite.head_sha;\n              }\n              if (!headSha) {\n                core.setOutput('skip', 'true');\n                return;\n              }")
content = content.replace("headSha = pulls.data[0].head.sha || context.payload.workflow_run.head_sha;\n              if (!headSha) {\n                core.setOutput('skip', 'true');\n                return;\n              }", "headSha = pulls.data[0].head.sha;\n              if (!headSha) {\n                headSha = context.payload.workflow_run.head_sha;\n              }\n              if (!headSha) {\n                core.setOutput('skip', 'true');\n                return;\n              }")

with open('.github/workflows/auto-merge.yml', 'w') as f:
    f.write(content)
