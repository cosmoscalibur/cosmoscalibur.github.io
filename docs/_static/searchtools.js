/**
* Simple result scoring code.
*/
if(Scorer===void 0)var Scorer={objNameMatch:11,objPartialMatch:6,objPrio:{0:15,1:5,2:-5},objPrioDefault:0,title:15,partialTitle:7,term:5,partialTerm:2};
// Global search result kind enum, used by themes to style search results.
class SearchResultKind{static get index(){return`index`}static get object(){return`object`}static get text(){return`text`}static get title(){return`title`}}const _removeChildren=element=>{for(;element&&element.lastChild;)element.removeChild(element.lastChild)},_escapeRegExp=string=>string.replace(/[.*+\-?^${}()|[\]\\]/g,`\\$&`),_displayItem=(item,searchTerms,highlightTerms)=>{let docBuilder=DOCUMENTATION_OPTIONS.BUILDER,docFileSuffix=DOCUMENTATION_OPTIONS.FILE_SUFFIX,docLinkSuffix=DOCUMENTATION_OPTIONS.LINK_SUFFIX,showSearchSummary=DOCUMENTATION_OPTIONS.SHOW_SEARCH_SUMMARY,contentRoot=document.documentElement.dataset.content_root,[docName,title,anchor,descr,score,_filename,kind]=item,listItem=document.createElement(`li`);
// Add a class representing the item's type:
// can be used by a theme's CSS selector for styling
// See SearchResultKind for the class names.
listItem.classList.add(`kind-${kind}`);let requestUrl,linkUrl;if(docBuilder===`dirhtml`){
// dirhtml builder
let dirname=docName+`/`;dirname.match(/\/index\/$/)?dirname=dirname.substring(0,dirname.length-6):dirname===`index/`&&(dirname=``),requestUrl=contentRoot+dirname,linkUrl=requestUrl}else requestUrl=contentRoot+docName+docFileSuffix,linkUrl=docName+docLinkSuffix;let linkEl=listItem.appendChild(document.createElement(`a`));linkEl.href=linkUrl+anchor,linkEl.dataset.score=score,linkEl.innerHTML=title,descr?(listItem.appendChild(document.createElement(`span`)).innerHTML=` (`+descr+`)`,SPHINX_HIGHLIGHT_ENABLED&&highlightTerms.forEach(term=>_highlightText(listItem,term,`highlighted`))):showSearchSummary&&fetch(requestUrl).then(responseData=>responseData.text()).then(data=>{
// highlight search terms in the summary
data&&listItem.appendChild(Search.makeSearchSummary(data,searchTerms,anchor)),SPHINX_HIGHLIGHT_ENABLED&&highlightTerms.forEach(term=>_highlightText(listItem,term,`highlighted`))}),Search.output.appendChild(listItem)},_finishSearch=resultCount=>{Search.stopPulse(),Search.title.innerText=_(`Search Results`),resultCount?Search.status.innerText=Documentation.ngettext(`Search finished, found one page matching the search query.`,"Search finished, found ${resultCount} pages matching the search query.",resultCount).replace("${resultCount}",resultCount):Search.status.innerText=Documentation.gettext(`Your search did not match any documents. Please make sure that all words are spelled correctly and that you've selected enough categories.`)},_displayNextItem=(results,resultCount,searchTerms,highlightTerms)=>{
// results left, load the summary and display it
// this is intended to be dynamic (don't sub resultsCount)
results.length?(_displayItem(results.pop(),searchTerms,highlightTerms),setTimeout(()=>_displayNextItem(results,resultCount,searchTerms,highlightTerms),5)):_finishSearch(resultCount)},_orderResultsByScoreThenName=(a,b)=>{let leftScore=a[4],rightScore=b[4];if(leftScore===rightScore){
// same score: sort alphabetically
let leftTitle=a[1].toLowerCase(),rightTitle=b[1].toLowerCase();return leftTitle===rightTitle?0:leftTitle>rightTitle?-1:1}return leftScore>rightScore?1:-1};
/**
* Default splitQuery function. Can be overridden in ``sphinx.search`` with a
* custom function per language.
*
* The regular expression works by splitting the string on consecutive characters
* that are not Unicode letters, numbers, underscores, or emoji characters.
* This is the same as ``\W+`` in Python, preserving the surrogate pair area.
*/
if(splitQuery===void 0)var splitQuery=query=>query.split(/[^\p{Letter}\p{Number}_\p{Emoji_Presentation}]+/gu).filter(term=>term);
/**
* Search Module
*/
const Search={_index:null,_queued_query:null,_pulse_status:-1,htmlToText:(htmlString,anchor)=>{let htmlElement=new DOMParser().parseFromString(htmlString,`text/html`);for(let removalQuery of[`.headerlink`,`script`,`style`])htmlElement.querySelectorAll(removalQuery).forEach(el=>{el.remove()});if(anchor){let anchorContent=htmlElement.querySelector(`[role="main"] ${anchor}`);if(anchorContent)return anchorContent.textContent;console.warn(`Anchored content block not found. Sphinx search tries to obtain it via DOM query '[role=main] ${anchor}'. Check your theme or template.`)}
// if anchor not specified or not found, fall back to main content
let docContent=htmlElement.querySelector(`[role="main"]`);return docContent?docContent.textContent:(console.warn(`Content block not found. Sphinx search tries to obtain it via DOM query '[role=main]'. Check your theme or template.`),``)},init:()=>{let query=new URLSearchParams(window.location.search).get(`q`);document.querySelectorAll(`input[name="q"]`).forEach(el=>el.value=query),query&&Search.performSearch(query)},loadIndex:url=>document.body.appendChild(document.createElement(`script`)).src=url,setIndex:index=>{if(Search._index=index,Search._queued_query!==null){let query=Search._queued_query;Search._queued_query=null,Search.query(query)}},hasIndex:()=>Search._index!==null,deferQuery:query=>Search._queued_query=query,stopPulse:()=>Search._pulse_status=-1,startPulse:()=>{if(Search._pulse_status>=0)return;let pulse=()=>{Search._pulse_status=(Search._pulse_status+1)%4,Search.dots.innerText=`.`.repeat(Search._pulse_status),Search._pulse_status>=0&&window.setTimeout(pulse,500)};pulse()},performSearch:query=>{
// create the required interface elements
let searchText=document.createElement(`h2`);searchText.textContent=_(`Searching`);let searchSummary=document.createElement(`p`);searchSummary.classList.add(`search-summary`),searchSummary.innerText=``;let searchList=document.createElement(`ul`);searchList.setAttribute(`role`,`list`),searchList.classList.add(`search`);let out=document.getElementById(`search-results`);Search.title=out.appendChild(searchText),Search.dots=Search.title.appendChild(document.createElement(`span`)),Search.status=out.appendChild(searchSummary),Search.output=out.appendChild(searchList);let searchProgress=document.getElementById(`search-progress`);
// index already loaded, the browser was quick!
searchProgress&&(searchProgress.innerText=_(`Preparing search...`)),Search.startPulse(),Search.hasIndex()?Search.query(query):Search.deferQuery(query)},_parseQuery:query=>{
// stem the search terms and add them to the correct list
let stemmer=new Stemmer,searchTerms=/* @__PURE__ */ new Set,excludedTerms=/* @__PURE__ */ new Set,highlightTerms=/* @__PURE__ */ new Set,objectTerms=new Set(splitQuery(query.toLowerCase().trim()));
// console.debug("SEARCH: searching for:");
// console.info("required: ", [...searchTerms]);
// console.info("excluded: ", [...excludedTerms]);
return splitQuery(query.trim()).forEach(queryTerm=>{let queryTermLower=queryTerm.toLowerCase();
// maybe skip this "word"
// stopwords array is from language_data.js
if(stopwords.indexOf(queryTermLower)!==-1||queryTerm.match(/^\d+$/))return;
// stem the word
let word=stemmer.stemWord(queryTermLower);
// select the correct list
word[0]===`-`?excludedTerms.add(word.substr(1)):(searchTerms.add(word),highlightTerms.add(queryTermLower))}),SPHINX_HIGHLIGHT_ENABLED&&localStorage.setItem(`sphinx_highlight_terms`,[...highlightTerms].join(` `)),[query,searchTerms,excludedTerms,highlightTerms,objectTerms]},_performSearch:(query,searchTerms,excludedTerms,highlightTerms,objectTerms)=>{let filenames=Search._index.filenames,docNames=Search._index.docnames,titles=Search._index.titles,allTitles=Search._index.alltitles,indexEntries=Search._index.indexentries,normalResults=[],nonMainIndexResults=[];_removeChildren(document.getElementById(`search-progress`));let queryLower=query.toLowerCase().trim();for(let[title,foundTitles]of Object.entries(allTitles))if(title.toLowerCase().trim().includes(queryLower)&&queryLower.length>=title.length/2)for(let[file,id]of foundTitles){let score=Math.round(Scorer.title*queryLower.length/title.length),boost=titles[file]===title?1:0;normalResults.push([docNames[file],titles[file]===title?title:`${titles[file]} > ${title}`,id===null?``:`#`+id,null,score+boost,filenames[file],SearchResultKind.title])}
// search for explicit entries in index directives
for(let[entry,foundEntries]of Object.entries(indexEntries))if(entry.includes(queryLower)&&queryLower.length>=entry.length/2)for(let[file,id,isMain]of foundEntries){let score=Math.round(100*queryLower.length/entry.length),result=[docNames[file],titles[file],id?`#`+id:``,null,score,filenames[file],SearchResultKind.index];isMain?normalResults.push(result):nonMainIndexResults.push(result)}objectTerms.forEach(term=>normalResults.push(...Search.performObjectSearch(term,objectTerms))),normalResults.push(...Search.performTermsSearch(searchTerms,excludedTerms)),Scorer.score&&(normalResults.forEach(item=>item[4]=Scorer.score(item)),nonMainIndexResults.forEach(item=>item[4]=Scorer.score(item))),normalResults.sort(_orderResultsByScoreThenName),nonMainIndexResults.sort(_orderResultsByScoreThenName);
// Combine the result groups in (reverse) order.
// Non-main index entries are typically arbitrary cross-references,
// so display them after other results.
let results=[...nonMainIndexResults,...normalResults],seen=/* @__PURE__ */ new Set;return results=results.reverse().reduce((acc,result)=>{let resultStr=result.slice(0,4).concat([result[5]]).map(v=>String(v)).join(`,`);return seen.has(resultStr)||(acc.push(result),seen.add(resultStr)),acc},[]),results.reverse()},query:query=>{let[searchQuery,searchTerms,excludedTerms,highlightTerms,objectTerms]=Search._parseQuery(query),results=Search._performSearch(searchQuery,searchTerms,excludedTerms,highlightTerms,objectTerms);
// for debugging
//Search.lastresults = results.slice();  // a copy
// console.info("search results:", Search.lastresults);
// print the results
_displayNextItem(results,results.length,searchTerms,highlightTerms)},performObjectSearch:(object,objectTerms)=>{let filenames=Search._index.filenames,docNames=Search._index.docnames,objects=Search._index.objects,objNames=Search._index.objnames,titles=Search._index.titles,results=[],objectSearchCallback=(prefix,match)=>{let name=match[4],fullname=(prefix?prefix+`.`:``)+name,fullnameLower=fullname.toLowerCase();if(fullnameLower.indexOf(object)<0)return;let score=0,parts=fullnameLower.split(`.`);
// check for different match types: exact matches of full name or
// "last name" (i.e. last dotted part)
fullnameLower===object||parts.slice(-1)[0]===object?score+=Scorer.objNameMatch:parts.slice(-1)[0].indexOf(object)>-1&&(score+=Scorer.objPartialMatch);let objName=objNames[match[1]][2],title=titles[match[0]],otherTerms=new Set(objectTerms);if(otherTerms.delete(object),otherTerms.size>0){let haystack=`${prefix} ${name} ${objName} ${title}`.toLowerCase();if([...otherTerms].some(otherTerm=>haystack.indexOf(otherTerm)<0))return}let anchor=match[3];anchor===``?anchor=fullname:anchor===`-`&&(anchor=objNames[match[1]][1]+`-`+fullname);let descr=objName+_(`, in `)+title;Scorer.objPrio.hasOwnProperty(match[2])?score+=Scorer.objPrio[match[2]]:score+=Scorer.objPrioDefault,results.push([docNames[match[0]],fullname,`#`+anchor,descr,score,filenames[match[0]],SearchResultKind.object])};return Object.keys(objects).forEach(prefix=>objects[prefix].forEach(array=>objectSearchCallback(prefix,array))),results},performTermsSearch:(searchTerms,excludedTerms)=>{
// prepare search
let terms=Search._index.terms,titleTerms=Search._index.titleterms,filenames=Search._index.filenames,docNames=Search._index.docnames,titles=Search._index.titles,scoreMap=/* @__PURE__ */ new Map,fileMap=/* @__PURE__ */ new Map;
// perform the search on the required terms
searchTerms.forEach(word=>{let files=[],arr=[{files:terms.hasOwnProperty(word)?terms[word]:void 0,score:Scorer.term},{files:titleTerms.hasOwnProperty(word)?titleTerms[word]:void 0,score:Scorer.title}];
// add support for partial matches
if(word.length>2){let escapedWord=_escapeRegExp(word);terms.hasOwnProperty(word)||Object.keys(terms).forEach(term=>{term.match(escapedWord)&&arr.push({files:terms[term],score:Scorer.partialTerm})}),titleTerms.hasOwnProperty(word)||Object.keys(titleTerms).forEach(term=>{term.match(escapedWord)&&arr.push({files:titleTerms[term],score:Scorer.partialTitle})})}arr.every(record=>record.files===void 0)||(arr.forEach(record=>{if(record.files===void 0)return;let recordFiles=record.files;
// set score for the word in each file
recordFiles.length===void 0&&(recordFiles=[recordFiles]),files.push(...recordFiles),recordFiles.forEach(file=>{scoreMap.has(file)||scoreMap.set(file,/* @__PURE__ */ new Map),scoreMap.get(file).set(word,record.score)})}),files.forEach(file=>{fileMap.has(file)?fileMap.get(file).indexOf(word)===-1&&fileMap.get(file).push(word):fileMap.set(file,[word])}))});
// now check if the files don't contain excluded terms
let results=[];for(let[file,wordList]of fileMap){
// check if all requirements are matched
// as search terms with length < 3 are discarded
let filteredTermCount=[...searchTerms].filter(term=>term.length>2).length;if(wordList.length!==searchTerms.size&&wordList.length!==filteredTermCount)continue;
// ensure that none of the excluded terms is in the search result
if([...excludedTerms].some(term=>terms[term]===file||titleTerms[term]===file||(terms[term]||[]).includes(file)||(titleTerms[term]||[]).includes(file)))break;
// select one (max) score for the file.
let score=Math.max(...wordList.map(w=>scoreMap.get(file).get(w)));
// add result to the result list
results.push([docNames[file],titles[file],``,null,score,filenames[file],SearchResultKind.text])}return results},makeSearchSummary:(htmlText,keywords,anchor)=>{let text=Search.htmlToText(htmlText,anchor);if(text===``)return null;let textLower=text.toLowerCase(),actualStartPosition=[...keywords].map(k=>textLower.indexOf(k.toLowerCase())).filter(i=>i>-1).slice(-1)[0],startWithContext=Math.max(actualStartPosition-120,0),top=startWithContext===0?``:`...`,tail=startWithContext+240<text.length?`...`:``,summary=document.createElement(`p`);return summary.classList.add(`context`),summary.textContent=top+text.substr(startWithContext,240).trim()+tail,summary}};_ready(Search.init);