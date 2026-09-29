from io import BytesIO
from pathlib import Path

import streamlit as st
from pydub import AudioSegment

st.set_page_config(page_title="Aplikacja Generowanie Napisów V2", page_icon="🎬")
st.title("🎬 Aplikacja Generowanie Napisów — V2")
st.subheader("V2 — wideo + wyodrębnienie dźwięku")

uploaded_video = st.file_uploader(
    "Wybierz plik wideo",
    type=["mp4", "mov", "m4v", "webm", "avi"],
)

if uploaded_video:
    video_bytes = uploaded_video.getvalue()
    st.markdown("### 1. Wideo")
    st.video(video_bytes)

    extension = Path(uploaded_video.name).suffix.lower().lstrip(".") or "mp4"
    try:
        audio = AudioSegment.from_file(BytesIO(video_bytes), format=extension)
        audio_buffer = BytesIO()
        audio.export(audio_buffer, format="mp3")
        audio_buffer.seek(0)

        st.markdown("### 2. Wyodrębniony dźwięk")
        st.audio(audio_buffer, format="audio/mp3")
        st.success("Dźwięk został wyodrębniony z wideo.")
    except Exception as exc:
        st.error("Nie udało się wyodrębnić dźwięku. Upewnij się, że FFmpeg jest dostępny.")
        st.exception(exc)
