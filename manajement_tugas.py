tasks = []
while True:
    
    print("\nDaftar Tugas:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    choice = input("\nTambahkan tugas baru (tekan 'oke' untuk keluar): ")
    if choice.lower() == 'oke':
        break
        
    else:
        tasks.append(choice)
print("\nTerima kasih! Daftar tugas Anda:")
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")
