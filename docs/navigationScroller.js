document.addEventListener("DOMContentLoaded",()=>{
    const nav = document.querySelector(".navigation-box")
    window.addEventListener('scroll',()=>{
        nav.style.top= (window.scrollY+10)+"px"
    })
    const nav_list = document.querySelector(".navigation-list")
    const Sections = Array.from(document.querySelectorAll("section"))
    const SectionIds = Sections.map(section=>section.id)
    const SectionTitle = Sections.map(section=>{
        let h3 = section.querySelector("h3") 
        if(h3) return h3.textContent.trim().replace(/\\/g,"")
    })
    for(let x=0;x<SectionIds.length;x++)
    {
        nav_list.insertAdjacentHTML("beforeend",`<li><a href="#${SectionIds[x]}">${(SectionTitle[x]!=undefined)?SectionTitle[x]:SectionIds[x]}</a></li>`)
    }
})
