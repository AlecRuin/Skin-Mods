const ModsArray=[
    "DMC5-Vergil-as-Yasuo",
    "DMC5-Doppelganger-as-Yasuo",
    "DMC5-Nero-as-Blitzcrank",
    "DMC5-Dante-as-Samira",
    "DMC5-Dante-as-Riven",
    "DMC5-V-as-Hwei",
    "DMC5-Vergil-as-Yone",
    "DMC5-Griffon-as-Smolder",
    "Full-Build-Gwen"
]
const ModsArrayWhitespace=[
    "DMC5 Vergil as Yasuo",
    "DMC5 Doppelganger as Yasuo",
    "DMC5 Nero as Blitzcrank",
    "DMC5 Dante as Samira",
    "DMC5 Dante as Riven",
    "DMC5 V as Hwei",
    "DMC5 Vergil as Yone",
    "DMC5 Griffon as Smolder",
    "Full Build Gwen"
]
function testing()
{
    console.log("hello world");
}
document.addEventListener("DOMContentLoaded",()=>{
    const Mod_List = document.querySelector(".Mod-List")
    const nav_list = document.querySelector(".navigation-list")
    let leftFlag=true;
    for(let x=0;x<ModsArray.length;x++)
    {
        Mod_List.insertAdjacentHTML("beforeend",
            `
            <section class="w-100 mbt-1rem mrl-1rem"  id=${ModsArray[x]}>
                <iframe class="preview-nugget ${(leftFlag?"float-left":"float-right")}" src=${"./iframes/"+encodeURIComponent(ModsArray[x])+".html"}></iframe>
            </section>
            `)
        nav_list.insertAdjacentHTML("beforeend",`<li><a href="#${ModsArray[x]}">${ModsArrayWhitespace[x]}</a></li>`)
        leftFlag=!leftFlag
    }
    const nav = document.querySelector(".navigation-box")
    window.addEventListener('scroll',()=>{
        nav.style.top= (window.scrollY+10)+"px"
    })
})