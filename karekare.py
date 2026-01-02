import cv2
import os

def extract_350_frames(video_path, output_folder):
    # Video dosyasını aç
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Video açılamadı.")
        return

    # Toplam kare sayısı
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"🎥 Toplam kare sayısı: {total_frames}")

    # Her kaç karede bir alınacağını hesapla
    step = max(total_frames // 200, 1)
    print(f"🔁 Her {step} karede bir alınacak.")

    # Klasörü oluştur
    os.makedirs(output_folder, exist_ok=True)

    saved_count = 0
    for i in range(0, total_frames, step):
        if saved_count >= 200:
            break
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            print(f"⚠️ Kare alınamadı: {i}")
            continue
        filename = f"ka_{saved_count:05d}.jpg"
        filepath = os.path.join(output_folder, filename)
        saved = cv2.imwrite(filepath, frame)
        if not saved:
            print(f"❌ Kaydedilemedi: {filename}")
        saved_count += 1

    cap.release()
    print(f"✅ Tamamlandı: {saved_count} kare kaydedildi → {output_folder}")

# === SENİN BİLGİLERİN ===
video_path = "/Volumes/UNTITLED/201_1000_1200/repaired_video.mp4"
output_folder = "/Users/cankisacik/Desktop/KARELER/201/201-1"

extract_350_frames(video_path, output_folder)
