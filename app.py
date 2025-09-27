import gradio as gr

def transcribe_fn(uploaded_audio, recorded_audio):
    # Prioritize uploaded file if both exist
    if uploaded_audio is not None:
        source = uploaded_audio
    elif recorded_audio is not None:
        source = recorded_audio
    else:
        return "No audio provided."

    # For now, just a placeholder
    return "Calling API here"

with gr.Blocks() as demo:
    gr.Markdown("## Simple Transcription Demo")

    with gr.Row():
        uploaded_audio = gr.Audio(type="filepath", label="Upload Audio")
        recorded_audio = gr.Audio(sources=["microphone"], type="filepath", label="Record Audio")

    transcribe_btn = gr.Button("Transcribe")
    output_text = gr.Textbox(label="Transcription Result")

    transcribe_btn.click(
        fn=transcribe_fn,
        inputs=[uploaded_audio, recorded_audio],
        outputs=output_text
    )

demo.launch()