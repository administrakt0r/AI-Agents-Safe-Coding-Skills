const fs = require('fs')
const body = fs.readFileSync('pr_description_final.md').toString()

const text = String(body || "");
const heading = text.match(/##\s+quality bar checklist\b/i);

const section = text.slice(heading.index).split(/\n##\s+/i, 2)[0];
const full_body = text.split(/\n##\s+/i, 2)[0]
console.log(!/-\s+\[\s\]/.test(section));
console.log(!/-\s+\[\s\]/.test(text));
