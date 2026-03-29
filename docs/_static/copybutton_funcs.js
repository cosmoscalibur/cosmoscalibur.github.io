function escapeRegExp(string){return string.replace(/[.*+?^${}()|[\]\\]/g,`\\$&`)}
/**
* Removes excluded text from a Node.
*
* @param {Node} target Node to filter.
* @param {string} exclude CSS selector of nodes to exclude.
* @returns {DOMString} Text from `target` with text removed.
*/
export function filterText(target,exclude){let clone=target.cloneNode(!0);return exclude&&clone.querySelectorAll(exclude).forEach(node=>node.remove()),clone.innerText}
// Callback when a copy button is clicked. Will be passed the node that was clicked
// should then grab the text and replace pieces of text that shouldn't be used in output
export function formatCopyText(textContent,copybuttonPromptText,isRegexp=!1,onlyCopyPromptLines=!0,removePrompts=!0,copyEmptyLines=!0,lineContinuationChar=``,hereDocDelim=``){var regexp,match,useLineCont=!!lineContinuationChar,useHereDoc=!!hereDocDelim;
// create regexp to capture prompt and remaining line
regexp=isRegexp?/* @__PURE__ */ RegExp(`^(`+copybuttonPromptText+`)(.*)`):/* @__PURE__ */ RegExp(`^(`+escapeRegExp(copybuttonPromptText)+`)(.*)`);let outputLines=[];var promptFound=!1,gotLineCont=!1,gotHereDoc=!1;let lineGotPrompt=[];for(let line of textContent.split(`
`))match=line.match(regexp),match||gotLineCont||gotHereDoc?(promptFound=regexp.test(line),lineGotPrompt.push(promptFound),removePrompts&&promptFound?outputLines.push(match[2]):outputLines.push(line),gotLineCont=line.endsWith(lineContinuationChar)&useLineCont,line.includes(hereDocDelim)&useHereDoc&&(gotHereDoc=!gotHereDoc)):onlyCopyPromptLines?copyEmptyLines&&line.trim()===``&&outputLines.push(line):outputLines.push(line);return lineGotPrompt.some(v=>v===!0)&&(textContent=outputLines.join(`
`)),textContent.endsWith(`
`)&&(textContent=textContent.slice(0,-1)),textContent}