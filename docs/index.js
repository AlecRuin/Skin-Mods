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
const videosarray=[
    "./media/videos/DMC5 Dante as Riven showcase.mp4",
    "./media/videos/DMC5 Dante as Samira showcase.mp4",
    "./media/videos/DMC5 Deadweight as Blitzcrank showcase.mp4",
    "./media/videos/DMC5 Doppelganger as Yasuo showcase.mp4",
    "./media/videos/DMC5 Nero as Blitzcrank 2.0 showcase.mp4",
    "./media/videos/DMC5 V as Hwei.mp4",
    "./media/videos/DMC5 Vergil as Yasuo 2.0 showcase.mp4",
    "./media/videos/DMC5 Vergil as Yasuo showcase.mp4",
    "./media/videos/DMC5 Vergil as Yone showcase.mp4",
    "./media/videos/Full Build Gwen example.mp4"
]
function changeVideo(VideoElement,SourceElement)
{
    SourceElement.src =videosarray[Math.floor(Math.random()*videosarray.length)] 
    VideoElement.load()
}


document.addEventListener("DOMContentLoaded",()=>{
    const Mod_List = document.querySelector(".Mod-List")
    let leftFlag=true;
    ModsArray.forEach((item)=>{
        Mod_List.insertAdjacentHTML("beforeend",
            `
            <div class="w-100 mbt-3rem mrl-1rem">
                <iframe class="preview-nugget ${(leftFlag?"float-left":"float-right")}" src=${"./iframes/"+encodeURIComponent(item)+".html"}></iframe>
            <div>
            `)
        leftFlag=!leftFlag
    })
    var vid1 = document.getElementById("vid1")
    var source1 = document.getElementById("vid1source")
    var vid2 = document.getElementById("vid2")
    var source2 = document.getElementById("vid2source")
    var vid3 = document.getElementById("vid3")
    var source3 = document.getElementById("vid3source")
    vid1.defaultPlaybackRate=1.5
    vid2.defaultPlaybackRate=1.5
    vid3.defaultPlaybackRate=1.5
    vid1.load()
    vid2.load()
    vid3.load()
    vid1.addEventListener("ended",()=>{
        console.log("video ended");
        changeVideo(vid1,source1)
    })
    vid2.addEventListener("ended",()=>{
        console.log("video ended");
        changeVideo(vid2,source2)
    })
    vid3.addEventListener("ended",()=>{
        console.log("video ended");
        changeVideo(vid3,source3)
    })
})