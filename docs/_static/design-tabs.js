// @ts-check
// Extra JS capability for selected tabs to be synced
// The selection is stored in local storage so that it persists across page loads.
/**
* @type {Record<string, HTMLElement[]>}
*/
let sd_id_to_elements={};const storageKeyPrefix=`sphinx-design-tab-id-`;
/**
* Create a key for a tab element.
* @param {HTMLElement} el - The tab element.
* @returns {[string, string, string] | null} - The key.
*
*/
function create_key(el){let syncId=el.getAttribute(`data-sync-id`),syncGroup=el.getAttribute(`data-sync-group`);return!syncId||!syncGroup?null:[syncGroup,syncId,syncGroup+`--`+syncId]}
/**
* Initialize the tab selection.
*
*/
function ready(){
// Find all tabs with sync data
/** @type {string[]} */
let groups=[];document.querySelectorAll(`.sd-tab-label`).forEach(label=>{if(label instanceof HTMLElement){let data=create_key(label);if(data){let[group,id,key]=data;if(label.onclick=onSDLabelClick,sd_id_to_elements[key]||(sd_id_to_elements[key]=[]),sd_id_to_elements[key].push(label),groups.indexOf(group)===-1){groups.push(group);
// Check if a specific tab has been selected via URL parameter
let tabParam=new URLSearchParams(window.location.search).get(group);tabParam&&(console.log(`sphinx-design: Selecting tab id for group '`+group+`' from URL parameter: `+tabParam),window.sessionStorage.setItem(storageKeyPrefix+group,tabParam))}window.sessionStorage.getItem(storageKeyPrefix+group)===id&&(label.previousElementSibling.checked=!0)}}})}
/**
*  Activate other tabs with the same sync id.
*
* @this {HTMLElement} - The element that was clicked.
*/
function onSDLabelClick(){let data=create_key(this);if(!data)return;let[group,id,key]=data;for(let label of sd_id_to_elements[key])label!==this&&(label.previousElementSibling.checked=!0);window.sessionStorage.setItem(storageKeyPrefix+group,id)}document.addEventListener(`DOMContentLoaded`,ready,!1);