const { hasQualityChecklist } = require("./tools/lib/workflow-contract");
const body = `Imported the image skill from the trusted source coreyhaines31/marketingskills after verifying it complies with the English-first policy, license compatibility, and passing the prompt injection safety scan.

Also updated the maintenance ledger with the new entry and added the dated run log.`;

console.log(hasQualityChecklist(body));
