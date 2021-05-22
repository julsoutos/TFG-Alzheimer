/*
* Wordfind.js
* (c) 2012 Bill, BunKat LLC.
* Wordfind is freely distributable under the MIT license.
* @documentation http://github.com/bunkat/wordfind
*/
(function(){

    "use strict";
    var n=function(){
        var n="abcdefghijklmnoprstuvwy",
        r=["horizontal","horizontalBack","vertical","verticalUp","diagonal","diagonalUp","diagonalBack","diagonalUpBack"],
        t={horizontal:function(n,r,t){return{x:n+t,y:r}},horizontalBack:function(n,r,t){return{x:n-t,y:r}},vertical:function(n,r,t){return{x:n,y:r+t}},verticalUp:function(n,r,t){return{x:n,y:r-t}},diagonal:function(n,r,t){return{x:n+t,y:r+t}},diagonalBack:function(n,r,t){return{x:n-t,y:r+t}},diagonalUp:function(n,r,t){return{x:n+t,y:r-t}},diagonalUpBack:function(n,r,t){return{x:n-t,y:r-t}}},
        o={horizontal:function(n,r,t,o,e){return o>=n+e},horizontalBack:function(n,r,t,o,e){return n+1>=e},vertical:function(n,r,t,o,e){return t>=r+e},verticalUp:function(n,r,t,o,e){return r+1>=e},diagonal:function(n,r,t,o,e){return o>=n+e&&t>=r+e},diagonalBack:function(n,r,t,o,e){return n+1>=e&&t>=r+e},diagonalUp:function(n,r,t,o,e){return o>=n+e&&r+1>=e},diagonalUpBack:function(n,r,t,o,e){return n+1>=e&&r+1>=e}},
        e={horizontal:function(n,r,t){return{x:0,y:r+1}},horizontalBack:function(n,r,t){return{x:t-1,y:r}},vertical:function(n,r,t){return{x:0,y:r+100}},verticalUp:function(n,r,t){return{x:0,y:t-1}},diagonal:function(n,r,t){return{x:0,y:r+1}},diagonalBack:function(n,r,t){return{x:t-1,y:n>=t-1?r+1:r}},diagonalUp:function(n,r,t){return{x:0,y:t-1>r?t-1:r+1}},diagonalUpBack:function(n,r,t){return{x:t-1,y:n>=t-1?r+1:r}}},
        i=function(n,r){var t,o,e,i=[];for(t=0;t<r.height;t++)for(i.push([]),o=0;o<r.width;o++)i[t].push("");for(t=0,e=n.length;e>t;t++)if(!a(i,r,n[t]))return null;return i},a=function(n,r,o){var e=l(n,r,o);if(0===e.length)return!1;var i=e[Math.floor(Math.random()*e.length)];return c(n,o,i.x,i.y,t[i.orientation]),!0},l=function(n,r,i){for(var a=[],l=r.height,c=r.width,h=i.length,g=0,v=0,p=r.orientations.length;p>v;v++)
            for(var d=r.orientations[v],s=o[d],x=t[d],y=e[d],k=0,B=0;l>B;)if(s(k,B,l,c,h)){var w=u(i,n,k,B,x);(w>=g||!r.preferOverlap&&w>-1)&&(g=w,a.push({x:k,y:B,orientation:d,overlap:w})),k++,k>=c&&(k=0,B++)}else{var U=y(k,B,h);k=U.x,B=U.y}return r.preferOverlap?f(a,g):a},u=function(n,r,t,o,e){for(var i=0,a=0,l=n.length;l>a;a++){var u=e(t,o,a),f=r[u.y][u.x];if(f===n[a])i++;else if(""!==f)return-1}return i},f=function(n,r){for(var t=[],o=0,e=n.length;e>o;o++)n[o].overlap>=r&&t.push(n[o]);return t},c=function(n,r,t,o,e){for(var i=0,a=r.length;a>i;i++){var l=e(t,o,i);n[l.y][l.x]=r[i]}};return{validOrientations:r,orientations:t,newPuzzle:function(n,t){var o,e,a=0,l=t||{};o=n.slice(0).sort(function(n,r){return n.length<r.length?1:0});for(var u={height:l.height||o[0].length,width:l.width||o[0].length,orientations:l.orientations||r,fillBlanks:void 0!==l.fillBlanks?l.fillBlanks:!0,maxAttempts:l.maxAttempts||3,preferOverlap:void 0!==l.preferOverlap?l.preferOverlap:!0};!e;){for(;!e&&a++<u.maxAttempts;)e=i(o,u);e||(u.height++,u.width++,a=0)}return u.fillBlanks&&this.fillBlanks(e,u),e},fillBlanks:function(r){for(var t=0,o=r.length;o>t;t++)for(var e=r[t],i=0,a=e.length;a>i;i++)if(!r[t][i]){var l=Math.floor(Math.random()*n.length);r[t][i]=n[l]}},solve:function(n,t){for(var o={height:n.length,width:n[0].length,orientations:r,preferOverlap:!0},e=[],i=[],a=0,u=t.length;u>a;a++){var f=t[a],c=l(n,o,f);c.length>0&&c[0].overlap===f.length?(c[0].word=f,e.push(c[0])):i.push(f)}return{found:e,notFound:i}},print:function(n){for(var r="",t=0,o=n.length;o>t;t++){for(var e=n[t],i=0,a=e.length;a>i;i++)r+=(""===e[i]?" ":e[i])+" ";r+="\n"}return console.log(r),r}}},r="undefined"!=typeof exports&&null!==exports?exports:window;r.wordfind=n()
        }).call(this);



    $(document).ready(function(){

        if(document.getElementById("load").innerHTML == "False"){
    
        // var audio1 = new Audio('../../static/assets/audios/letter.mp3');   
        // audio1.play();
    
            setTimeout(() => {document.getElementById("continue").click()}, 5000)
    
        }
    
        if(document.getElementById("load").innerHTML == "True"){
           
            puzzle = createPuzzle(document.getElementById("variant"))
            
            letters = document.getElementsByName('letter')

            
            for (let index = 0; index < puzzle.length; index++) {
                
                letter = letters[index] 
                letter.innerHTML = puzzle[index]
                                
            }
          
    
        }

    
    });

function createPuzzle(value){
    res = []

    var words = [document.getElementById("variant").innerHTML];
    
    var puzzle = wordfind.newPuzzle(words, {
        // Establecer dimensiones del rompecabezas
        height: 5,
        width:  6,
        //Orientaciones posibles de las palabras
        orientations: ["horizontal","horizontalBack","vertical","verticalUp","diagonal","diagonalUp","diagonalBack","diagonalUpBack"],
        // Establecer un carácter aleatorio los espacios vacíos
        fillBlanks: true,
        preferOverlap: false
    });

    for (let index = 0; index < puzzle.length ; index++) {
        
        res.push(...puzzle[index])
        
     }

     return res
}

function set(element){
    
    element.style.background = "#81D3D4"
    document.getElementById("answer").value = document.getElementById("answer").value != undefined ? document.getElementById("answer").value + element.innerHTML : element.innerHTML
}


function reset(){

    document.getElementById("answer").value = ""    
    letters = document.getElementsByName('letter')
    for (let index = 0; index < letters.length; index++) {
        letters[index].style.background = "white"        
    }

}