const fs = require('fs')
const body = fs.readFileSync('pr_description_2.md').toString()

const text = String(body || "");
const heading = text.match(/##\s+quality bar checklist\b/i);
console.log(heading.index)

const section = text.slice(heading.index).split(/\n##\s+/i, 2)[0];
console.log("SECTION:")
console.log(section)
console.log(/-\s+\[[xX]\]/.test(section))
console.log(!/-\s+\[\s\]/.test(section));
