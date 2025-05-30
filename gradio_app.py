# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv # type: ignore
load_dotenv()

#VoiceBot UI with Gradio
import os
import gradio as gr # type: ignore

from drbrain import encode_image, analyze_image_with_query
from patientvoice import record_audio
from patientvoice import transcribe_with_groq

from doctorvoice import text_to_speech_with_gtts
from doctorvoice import text_to_speech_with_elevenlabs

load_dotenv()

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query= system_prompt+ speech_to_text_output, encoded_image=encode_image(image_filepath), model="llama-3.2-11b-vision-preview")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(input_text= doctor_response, output_filepath="final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="This is what you said"),
        gr.Textbox(label="This is what Doctor Says"),
        gr.Audio("Temp.mp3")
    ],
    title="Dr. Vani - Your Virtual Doctor"
)

iface.launch(debug=True)

#http://127.0.0.1:7860