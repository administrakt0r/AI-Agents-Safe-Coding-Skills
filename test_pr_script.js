const {hasQualityChecklist} = require("./tools/lib/workflow-contract");
const fs = require('fs');
let validPR = fs.readFileSync('.github/PULL_REQUEST_TEMPLATE.md', 'utf8');
validPR = validPR.replace(/- \[ \] /g, '- [x] ');
console.log(hasQualityChecklist(validPR));
