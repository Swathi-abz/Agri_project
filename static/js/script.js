// ==========================
// Ask AI
// ==========================

function askAI() {

    const question = document.getElementById("question").value.trim();
    const responseBox = document.getElementById("response");
    const audioPlayer = document.getElementById("audioPlayer");

    if (question === "") {
        responseBox.innerHTML =
            "<span style='color:red;'>Please enter your question.</span>";
        return;
    }

    responseBox.innerHTML = "<b>Thinking...</b>";

    fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question
        })

    })

    .then(res => res.json())

    .then(data => {

        console.log(data);

        if (data.error) {

            responseBox.innerHTML =
                "<span style='color:red;'>" + data.error + "</span>";

            return;
        }

        responseBox.innerHTML = `

<b>🌐 Language:</b> ${data.language}<br><br>

<b>📝 Translated Question:</b><br>
${data.translated_question}<br><br>

<b>🎯 Intent:</b><br>
${data.intent}<br><br>

<b>🌱 Entities:</b><br>

Crop : ${data.entities.crop || "None"}<br>

Disease : ${data.entities.disease || "None"}<br>

Fertilizer : ${data.entities.fertilizer || "None"}<br><br>

<b>🤖 AI Response:</b><br>

${data.response.replace(/\n/g,"<br>")}

`;

        if (data.audio) {

            audioPlayer.src =
                "/" + data.audio + "?t=" + new Date().getTime();

            audioPlayer.load();

            audioPlayer.play().catch(() => {});

        }

    })

    .catch(err => {

        console.log(err);

        responseBox.innerHTML =
            "<span style='color:red;'>Server Error</span>";

    });

}



// ==========================
// Enter Key
// ==========================

document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("question")

    .addEventListener("keypress", function(e){

        if(e.key==="Enter"){

            askAI();

        }

    });

});



// ==========================
// Voice Recording
// ==========================

let mediaRecorder;

let audioChunks = [];

async function startRecording() {

    try {

        const stream =
            await navigator.mediaDevices.getUserMedia({
                audio: true
            });

        let mimeType = "audio/webm";

        if (
            MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
        ) {

            mimeType = "audio/webm;codecs=opus";

        }

        mediaRecorder = new MediaRecorder(stream, {
            mimeType: mimeType
        });

        audioChunks = [];

        mediaRecorder.ondataavailable = function(e){

            if(e.data.size > 0){

                audioChunks.push(e.data);

            }

        };

        mediaRecorder.onstop = function(){

            stream.getTracks().forEach(track => track.stop());

            sendAudio();

        };

        mediaRecorder.start();

        alert("🎤 Speak now...");

        setTimeout(function(){

            mediaRecorder.stop();

        },5000);

    }

    catch(err){

        console.log(err);

        alert("Microphone permission denied.");

    }

}



// ==========================
// Send Audio
// ==========================

function sendAudio(){

    const blob = new Blob(audioChunks,{
        type: mediaRecorder.mimeType
    });

    if(blob.size===0){

        alert("No audio recorded.");

        return;

    }

    const formData = new FormData();

    formData.append(
        "audio",
        blob,
        "voice.webm"
    );

    fetch("/voice",{

        method:"POST",

        body:formData

    })

    .then(res=>res.json())

    .then(data=>{

        console.log(data);

        if(data.error){

            alert(data.error);

            return;

        }

        document.getElementById("question").value=data.text;

        document.getElementById("response").innerHTML=`

<b>🎤 Recognized Speech</b><br>

${data.text}<br><br>

<b>🤖 AI Response</b><br>

${data.response.replace(/\n/g,"<br>")}

`;

        if(data.audio){

            const player=document.getElementById("audioPlayer");

            player.src="/" + data.audio + "?t=" + new Date().getTime();

            player.load();

            player.play().catch(()=>{});

        }

    })

    .catch(err=>{

        console.log(err);

        alert("Voice recognition failed.");

    });

}