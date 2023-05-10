"""
This file would contain code for saving the video on the local computer.
Here, functions could be defined to save the video file to a specific location.
"""
import imageio
import io

# stream de bytes del video (ejemplo)
video_bytes = b'\x00\x01\x02\x03\x04'

# crear un objeto io.BytesIO a partir del stream de bytes
video_io = io.BytesIO(video_bytes)

# cargar el stream de bytes en un objeto imageio
video_reader = imageio.read_reader(video_io, '.mp4')

# crear un objeto writer de imageio para escribir el archivo de salida
writer = imageio.get_writer('video.mp4')

# agregar cada frame del video al objeto writer de imageio
for frame in video_reader:
    writer.append_data(frame)

# cerrar el objeto writer de imageio
writer.close()
