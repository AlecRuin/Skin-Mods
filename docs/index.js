const ModsArray=[
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
document.addEventListener("DOMContentLoaded",()=>{
    const Mod_List = document.querySelector(".Mod-List")
    let leftFlag=true;
    ModsArray.forEach((item)=>{
        Mod_List.insertAdjacentHTML("beforeend",
            `
            <div class="w-100 mbt-1rem mrl-1rem">
                <iframe class="preview-nugget ${(leftFlag?"float-left":"float-right")}" src=${"./iframes/"+encodeURIComponent(item)+".html"}></iframe>
            <div>
            `)
        leftFlag=!leftFlag
    })
})