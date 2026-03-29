// Localization support
const messages={en:{copy:`Copy`,copy_to_clipboard:`Copy to clipboard`,copy_success:`Copied!`,copy_failure:`Failed to copy`},es:{copy:`Copiar`,copy_to_clipboard:`Copiar al portapapeles`,copy_success:`¡Copiado!`,copy_failure:`Error al copiar`},de:{copy:`Kopieren`,copy_to_clipboard:`In die Zwischenablage kopieren`,copy_success:`Kopiert!`,copy_failure:`Fehler beim Kopieren`},fr:{copy:`Copier`,copy_to_clipboard:`Copier dans le presse-papier`,copy_success:`Copié !`,copy_failure:`Échec de la copie`},ru:{copy:`Скопировать`,copy_to_clipboard:`Скопировать в буфер`,copy_success:`Скопировано!`,copy_failure:`Не удалось скопировать`},"zh-CN":{copy:`复制`,copy_to_clipboard:`复制到剪贴板`,copy_success:`复制成功!`,copy_failure:`复制失败`},it:{copy:`Copiare`,copy_to_clipboard:`Copiato negli appunti`,copy_success:`Copiato!`,copy_failure:`Errore durante la copia`}};let locale=`en`;document.documentElement.lang!==void 0&&messages[document.documentElement.lang]!==void 0&&(locale=document.documentElement.lang);let doc_url_root=DOCUMENTATION_OPTIONS.URL_ROOT;doc_url_root==`#`&&(doc_url_root=``);
/**
* SVG files for our copy buttons
*/
let iconCheck=`<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-check" width="44" height="44" viewBox="0 0 24 24" stroke-width="2" stroke="#22863a" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <title>${messages[locale].copy_success}</title>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M5 12l5 5l10 -10" />
</svg>`,iconCopy=``;iconCopy||=`<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <title>${messages[locale].copy_to_clipboard}</title>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <rect x="8" y="8" width="12" height="12" rx="2" />
  <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2" />
</svg>`;
/**
* Set up copy/paste for code blocks
*/
const runWhenDOMLoaded=cb=>{document.readyState==`loading`?document.addEventListener?document.addEventListener(`DOMContentLoaded`,cb):document.attachEvent(`onreadystatechange`,function(){document.readyState==`complete`&&cb()}):cb()},codeCellId=index=>`codecell${index}`,clearSelection=()=>{window.getSelection?window.getSelection().removeAllRanges():document.selection&&document.selection.empty()};
// Changes tooltip text for a moment, then changes it back
// We want the timeout of our `success` class to be a bit shorter than the
// tooltip and icon change, so that we can hide the icon before changing back.
var timeoutIcon=2e3,timeoutSuccessClass=1500;const temporarilyChangeTooltip=(el,oldText,newText)=>{el.setAttribute(`data-tooltip`,newText),el.classList.add(`success`),setTimeout(()=>el.classList.remove(`success`),timeoutSuccessClass),setTimeout(()=>el.setAttribute(`data-tooltip`,oldText),timeoutIcon)},temporarilyChangeIcon=el=>{el.innerHTML=iconCheck,setTimeout(()=>{el.innerHTML=iconCopy},timeoutIcon)},addCopyButtonToCodeCells=()=>{
// If ClipboardJS hasn't loaded, wait a bit and try again. This
// happens because we load ClipboardJS asynchronously.
if(window.ClipboardJS===void 0){setTimeout(addCopyButtonToCodeCells,250);return}
// Add copybuttons to all of our code cells
let COPYBUTTON_SELECTOR=`div.highlight pre`;document.querySelectorAll(`div.highlight pre`).forEach((codeCell,index)=>{let id=codeCellId(index);codeCell.setAttribute(`id`,id);let clipboardButton=id=>`<button class="copybtn o-tooltip--left" data-tooltip="${messages[locale].copy}" data-clipboard-target="#${id}">
      ${iconCopy}
    </button>`;codeCell.insertAdjacentHTML(`afterend`,clipboardButton(id))});function escapeRegExp(string){return string.replace(/[.*+?^${}()|[\]\\]/g,`\\$&`)}
/**
* Removes excluded text from a Node.
*
* @param {Node} target Node to filter.
* @param {string} exclude CSS selector of nodes to exclude.
* @returns {DOMString} Text from `target` with text removed.
*/
function filterText(target,exclude){let clone=target.cloneNode(!0);return exclude&&clone.querySelectorAll(exclude).forEach(node=>node.remove()),clone.innerText}
// Callback when a copy button is clicked. Will be passed the node that was clicked
// should then grab the text and replace pieces of text that shouldn't be used in output
function formatCopyText(textContent,copybuttonPromptText,isRegexp=!1,onlyCopyPromptLines=!0,removePrompts=!0,copyEmptyLines=!0,lineContinuationChar=``,hereDocDelim=``){var regexp,match,useLineCont=!!lineContinuationChar,useHereDoc=!!hereDocDelim;
// create regexp to capture prompt and remaining line
regexp=isRegexp?/* @__PURE__ */ RegExp(`^(`+copybuttonPromptText+`)(.*)`):/* @__PURE__ */ RegExp(`^(`+escapeRegExp(copybuttonPromptText)+`)(.*)`);let outputLines=[];var promptFound=!1,gotLineCont=!1,gotHereDoc=!1;let lineGotPrompt=[];for(let line of textContent.split(`
`))match=line.match(regexp),match||gotLineCont||gotHereDoc?(promptFound=regexp.test(line),lineGotPrompt.push(promptFound),removePrompts&&promptFound?outputLines.push(match[2]):outputLines.push(line),gotLineCont=line.endsWith(lineContinuationChar)&useLineCont,line.includes(hereDocDelim)&useHereDoc&&(gotHereDoc=!gotHereDoc)):onlyCopyPromptLines?copyEmptyLines&&line.trim()===``&&outputLines.push(line):outputLines.push(line);return lineGotPrompt.some(v=>v===!0)&&(textContent=outputLines.join(`
`)),textContent.endsWith(`
`)&&(textContent=textContent.slice(0,-1)),textContent}var copyTargetText=trigger=>{var target=document.querySelector(trigger.attributes[`data-clipboard-target`].value);
// get filtered text
let exclude=`.linenos`;return formatCopyText(filterText(target,`.linenos`),``,!1,!0,!0,!0,``,``)};
// Initialize with a callback so we can modify the text before copy
let clipboard=new ClipboardJS(`.copybtn`,{text:copyTargetText});clipboard.on(`success`,event=>{clearSelection(),temporarilyChangeTooltip(event.trigger,messages[locale].copy,messages[locale].copy_success),temporarilyChangeIcon(event.trigger)}),clipboard.on(`error`,event=>{temporarilyChangeTooltip(event.trigger,messages[locale].copy,messages[locale].copy_failure)})};runWhenDOMLoaded(addCopyButtonToCodeCells);