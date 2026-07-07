1. **Claim the Skill in Ledger**
   - Use the following Python script via bash heredoc to add an entry for `"skills/aws-penetration-testing"` into `data/maintenance/ledger.json` under the `"entries"` dict. Set `status` to `"active"`, `reviewerAgent` to `"malicious-skill-safety-auditor"`, and record the current date `2026-06-16`.
     ```bash
     cat << 'PY_EOF' > update_ledger_start.py
     import json

     with open('data/maintenance/ledger.json', 'r') as f:
         ledger = json.load(f)

     ledger['entries']['skills/aws-penetration-testing'] = {
         "status": "active",
         "lastReviewedAt": "2026-06-16",
         "reviewerAgent": "malicious-skill-safety-auditor",
         "outcome": "In progress",
         "linkedIssueOrPr": "",
         "nextAction": ""
     }

     with open('data/maintenance/ledger.json', 'w') as f:
         json.dump(ledger, f, indent=2)
     PY_EOF
     python3 update_ledger_start.py
     rm update_ledger_start.py
     ```
   - Verify the update using `cat data/maintenance/ledger.json | grep -A 5 -B 5 aws-penetration-testing`.

2. **Harden `skills/aws-penetration-testing/SKILL.md`**
   - Apply `replace_with_git_merge_diff` to update the frontmatter to the modernized schema and insert the "⚠️ AUTHORIZED USE ONLY" disclaimer:
     ```
     <<<<<<< SEARCH
     ---
     name: aws-penetration-testing
     description: "Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation, Lambda code extraction, and persistence techniques for red team operations."
     risk: unknown
     source: community
     author: zebbern
     date_added: "2026-02-27"
     ---

     # AWS Penetration Testing
     =======
     ---
     name: aws-penetration-testing
     description: "Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation, Lambda code extraction, and persistence techniques for red team operations."
     metadata:
       risk: offensive
       source: community
     author: zebbern
     date_added: "2026-02-27"
     ---

     > **⚠️ AUTHORIZED USE ONLY**
     > This skill is for educational purposes or authorized security assessments only.
     > You must have explicit, written permission from the system owner before using this tool.
     > Misuse of this tool is illegal and strictly prohibited.

     # AWS Penetration Testing
     >>>>>>> REPLACE
     ```
   - Apply `replace_with_git_merge_diff` to insert user confirmation in Inputs/Prerequisites:
     ```
     <<<<<<< SEARCH
     ## Inputs/Prerequisites

     - AWS CLI configured with credentials
     =======
     ## Inputs/Prerequisites

     - **Mandatory User Confirmation:** Ask the user to verify the target URL/IP before running any commands.
     - AWS CLI configured with credentials
     >>>>>>> REPLACE
     ```
   - Apply `replace_with_git_merge_diff` to replace the malicious python script and lambda zip upload:
     ```
     <<<<<<< SEARCH
     ### Lambda Privilege Escalation

     ```python
     # code.py - Inject into Lambda function
     import boto3

     def lambda_handler(event, context):
         client = boto3.client('iam')
         response = client.attach_user_policy(
             UserName='my_username',
             PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
         )
         return response
     ```

     ```bash
     # Update Lambda code
     aws lambda update-function-code --function-name target_function \
       --zip-file fileb://malicious.zip
     ```
     =======
     ### Lambda Privilege Escalation

     ```python
     # code.py - Inject into Lambda function
     # [SAFE-PAYLOAD] Simulate Lambda privilege escalation...
     ```

     ```bash
     # Update Lambda code
     # [SAFE-PAYLOAD] aws lambda update-function-code...
     ```
     >>>>>>> REPLACE
     ```
   - Use `sed -i` to replace the URLs in the Examples section:
     ```bash
     sed -i 's|https://app.com/proxy?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/|https://[SAFE-PAYLOAD]/proxy?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/|g' skills/aws-penetration-testing/SKILL.md
     ```
   - Verify the changes using `cat skills/aws-penetration-testing/SKILL.md`.

3. **Harden `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`**
   - Apply `replace_with_git_merge_diff` to replace the Lambda backdoor python code and the update-function-code command:
     ```
     <<<<<<< SEARCH
     ### Lambda Backdooring

     ```python
     # Malicious Lambda code to escalate privileges
     import boto3
     import json

     def handler(event, context):
         iam = boto3.client("iam")
         iam.attach_role_policy(
             RoleName="role_name",
             PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
         )
         iam.attach_user_policy(
             UserName="user_name",
             PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
         )
         return {'statusCode': 200, 'body': json.dumps("Pwned")}
     ```

     ```bash
     # Update function with backdoor
     aws lambda update-function-code --function-name NAME --zip-file fileb://backdoor.zip

     # Invoke backdoored function
     curl https://API_ID.execute-api.REGION.amazonaws.com/STAGE/ENDPOINT
     ```
     =======
     ### Lambda Backdooring

     ```python
     # Malicious Lambda code to escalate privileges
     # [SAFE-PAYLOAD] Simulate Lambda backdooring...
     ```

     ```bash
     # Update function with backdoor
     # [SAFE-PAYLOAD] aws lambda update-function-code...

     # Invoke backdoored function
     curl https://[SAFE-PAYLOAD]/STAGE/ENDPOINT
     ```
     >>>>>>> REPLACE
     ```
   - Apply `replace_with_git_merge_diff` to replace the container backdooring commands:
     ```
     <<<<<<< SEARCH
     ### Container Backdooring

     ```bash
     # Authenticate Docker to ECR
     aws ecr get-login-password --region REGION | docker login --username AWS --password-stdin ECR_ADDR

     # Build backdoored image
     docker build -t image_name .

     # Tag for ECR
     docker tag image_name ECR_ADDR:IMAGE_NAME

     # Push to ECR
     docker push ECR_ADDR:IMAGE_NAME
     ```
     =======
     ### Container Backdooring

     ```bash
     # Authenticate Docker to ECR
     aws ecr get-login-password --region REGION | docker login --username AWS --password-stdin ECR_ADDR

     # [SAFE-PAYLOAD] docker build/tag/push...
     ```
     >>>>>>> REPLACE
     ```
   - Apply `replace_with_git_merge_diff` to replace EKS Secrets via RCE URLs:
     ```
     <<<<<<< SEARCH
     ### EKS Secrets via RCE

     ```bash
     # List Kubernetes secrets
     https://website.com/rce.php?cmd=ls /var/run/secrets/kubernetes.io/serviceaccount

     # Get service account token
     https://website.com/rce.php?cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token
     ```
     =======
     ### EKS Secrets via RCE

     ```bash
     # List Kubernetes secrets
     https://[SAFE-PAYLOAD]/rce.php?cmd=ls /var/run/secrets/kubernetes.io/serviceaccount

     # Get service account token
     https://[SAFE-PAYLOAD]/rce.php?cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token
     ```
     >>>>>>> REPLACE
     ```
   - Verify the changes using `cat skills/aws-penetration-testing/references/advanced-aws-pentesting.md`.

4. **Verify, Test, and Revert Auto-generated Changes**
   - Run `npm install && ENABLE_NETWORK_TESTS=1 npm run test && npm run validate` across the repository.
   - Discard auto-generated changes to files like `CATALOG.md`, `data/catalog.json`, and `data/bundles.json` using `git restore --staged CATALOG.md data/catalog.json data/bundles.json` followed by `git checkout CATALOG.md data/catalog.json data/bundles.json`.
   - Run `git status` to verify the working tree is clean except for the intended files.

5. **Update Ledger with Final Status**
   - Use the following Python script via bash heredoc to update the entry in `data/maintenance/ledger.json` for `"skills/aws-penetration-testing"`.
     ```bash
     cat << 'PY_EOF' > update_ledger_end.py
     import json

     with open('data/maintenance/ledger.json', 'r') as f:
         ledger = json.load(f)

     ledger['entries']['skills/aws-penetration-testing']['status'] = "normalized"
     ledger['entries']['skills/aws-penetration-testing']['outcome'] = "Hardened skill by replacing active payloads with safe placeholders, added offensive disclaimer, and mandatory user confirmation."
     ledger['entries']['skills/aws-penetration-testing']['linkedIssueOrPr'] = "PR-aws-penetration-testing-hardening"
     ledger['entries']['skills/aws-penetration-testing']['nextAction'] = "Monitor for re-introduction of active payloads."

     with open('data/maintenance/ledger.json', 'w') as f:
         json.dump(ledger, f, indent=2)
     PY_EOF
     python3 update_ledger_end.py
     rm update_ledger_end.py
     ```
   - Verify the ledger update using `cat data/maintenance/ledger.json | grep -A 5 -B 5 aws-penetration-testing`.

6. **Create Run Log**
   - Create a run log at `docs/maintainers/agent-runs/2026-06-16-malicious-skill-safety-auditor-aws-penetration-testing.md` by embedding the exact literal markdown text inside a bash heredoc.
     ```bash
     cat << 'LOG_EOF' > docs/maintainers/agent-runs/2026-06-16-malicious-skill-safety-auditor-aws-penetration-testing.md
     # Run Log: 2026-06-16

     **Target:** `skills/aws-penetration-testing`

     **Why Selected:** High-risk offensive skill not yet present in the maintenance ledger and missing necessary safety guardrails such as the authorized use only disclaimer, mandatory user confirmation instructions, and contained active exploit payloads.

     **Evidence Reviewed:**
     - `skills/aws-penetration-testing/SKILL.md`: Frontmatter missing proper modernized schema and offensive risk level. Missing mandatory "⚠️ AUTHORIZED USE ONLY" disclaimer. Missing mandatory user confirmation for offensive attacks. Contains active payloads such as Lambda zip uploads and reverse shell/backdoor python code.
     - `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Contains active payloads for Lambda backdooring, Container Backdooring with Docker build/push, and URLs targeting simulated external systems.

     **Files Changed:**
     - `skills/aws-penetration-testing/SKILL.md`: Updated frontmatter to modernized schema, added AUTHORIZED USE ONLY disclaimer, added mandatory user confirmation, and replaced active exploitation payloads with `[SAFE-PAYLOAD]`.
     - `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Replaced active payloads with safe placeholders.
     - `data/maintenance/ledger.json`: Added entry for `skills/aws-penetration-testing`.

     **Linked PR:** PR-aws-penetration-testing-hardening

     **Next Action:** Monitor for re-introduction of active payloads.
     LOG_EOF
     ```
   - Verify the run log creation using `cat docs/maintainers/agent-runs/2026-06-16-malicious-skill-safety-auditor-aws-penetration-testing.md`.

7. **Pre-commit Steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

8. **Submit PR**
   - Call the `submit` tool to push the changes, using the branch name `aws-pentest-hardening` and providing the required PR description including the exact 'Quality Bar Checklist' extracted from `.github/PULL_REQUEST_TEMPLATE.md`:
     ```
     Fixes #N

     ## Quality Bar Checklist ✅

     **All items must be checked before merging.**

     - [ ] **Standards**: I have read `docs/contributors/quality-bar.md` and `docs/contributors/security-guardrails.md`.
     - [ ] **Metadata**: The `SKILL.md` frontmatter is valid (checked with `npm run validate`).
     - [ ] **Risk Label**: I have assigned the correct `risk:` tag (`none`, `safe`, `critical`, `offensive`, or `unknown` for legacy/unclassified content).
     - [ ] **Triggers**: The "When to use" section is clear and specific.
     - [ ] **Security**: If this is an _offensive_ skill, I included the "Authorized Use Only" disclaimer.
     - [ ] **Safety scan**: If this PR adds or modifies `SKILL.md` command guidance, remote/network examples, or token-like strings, I ran `npm run security:docs` (or equivalent hardening check) and addressed any findings.
     - [ ] **Automated Skill Review**: If this PR changes `SKILL.md`, I checked the `skill-review` GitHub Actions result and addressed any actionable feedback.
     - [ ] **Local Test**: I have verified the skill works locally.
     - [ ] **Repo Checks**: I ran `npm run validate:references` if my change affected docs, workflows, or infrastructure.
     - [ ] **Source-Only PR**: I did not manually include generated registry artifacts (`CATALOG.md`, `skills_index.json`, `data/*.json`) in this PR.
     - [ ] **Credits**: I have added the source credit in `README.md` (if applicable).
     - [ ] **Maintainer Edits**: I enabled **Allow edits from maintainers** on the PR.

     ## Screenshots (if applicable)
     ```
