from telethon import TelegramClient, events
import logging

# Konfigurasi Logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Konfigurasi
API_ID = '25453551'
API_HASH = 'c07ca7ee12f0a48fd5d506e556561331'
PHONE_NUMBER = '+628388444144'  # Ganti dengan nomor telepon yang terdaftar pada akun Telegram Anda
FROM_CHANNEL = 'https://t.me/Prediksi_togel_tanteJitu'
TO_CHANNELS = ['https://t.me/slot_gacor_sensasional', 'https://t.me/top_sniper','https://t.me/pejuang_angka','https://t.me/+uyLgUPw_vSNiYjhl', 'https://t.me/ampuh_jitu','https://t.me/kolabaangka','https://t.me/pecinta_tog3l', 'https://t.me/paito_jutawan','https://t.me/dunia_hibur','https://t.me/prediksi_angka_jitu', 'https://t.me/ruang_angka','https://t.me/info_slot_dan_togel_gacor','https://t.me/bocoran_angk4', 'https://t.me/hoki_jitu','https://t.me/master_angka','https://t.me/+M0cnniFG5xZlYzA1', 'https://t.me/pemburu_angka','https://t.me/pemburu_Cu4an', 'https://t.me/Racikan_angka','https://t.me/WAJIB_JPMASAL','https://t.me/Angka_M4in', 'https://t.me/prediksi_j1tu','https://t.me/pemburuBand0t','https://t.me/angkaToge1', 'https://t.me/kuliah_angka','https://t.me/angka_prediksi_togel','https://t.me/slot_sensaional', 'https://t.me/slot_gacoor','https://t.me/pusat_prediksiTogel', 'https://t.me/bigwin_slotgacor','https://t.me/komunitasSlot']

# Membuat Klien Telegram
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

# Menjalankan Klien
@client.on(events.NewMessage(chats=FROM_CHANNEL))
async def forward_message(event):
    try:
        for channel in TO_CHANNELS:
            if event.message.media:
                await client.send_file(channel, event.message.media)
            else:
                await client.send_message(channel, event.message.message)
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("Bot has started.")

with client:
    client.run_until_disconnected()
