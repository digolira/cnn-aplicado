import os
import shutil
from sklearn.model_selection import train_test_split

# Diretório onde estão armazenadas todas as classes
dataset_dir = './all'

# Diretório onde iremos salvar a divisão de treino, validação e teste
base_dir = '.'
os.makedirs(base_dir, exist_ok=True)

train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')

# Função para criar subpastas
def create_subdirs(base_path, classes):
    for cls in classes:
        os.makedirs(os.path.join(base_path, cls), exist_ok=True)

# Criar subdiretórios para treino, validação e teste
classes = os.listdir(dataset_dir)
create_subdirs(train_dir, classes)
create_subdirs(val_dir, classes)
create_subdirs(test_dir, classes)

# Divisão dos arquivos para cada classe
for cls in classes:
    cls_path = os.path.join(dataset_dir, cls)
    images = os.listdir(cls_path)
    
    # Dividir os arquivos da classe em 70% treino, 15% validação e 15% teste
    train_files, temp_files = train_test_split(images, test_size=0.3, random_state=42)
    val_files, test_files = train_test_split(temp_files, test_size=0.5, random_state=42)

    # Copiar os arquivos para as respectivas pastas
    for file in train_files:
        shutil.copy(os.path.join(cls_path, file), os.path.join(train_dir, cls))
    for file in val_files:
        shutil.copy(os.path.join(cls_path, file), os.path.join(val_dir, cls))
    for file in test_files:
        shutil.copy(os.path.join(cls_path, file), os.path.join(test_dir, cls))

print('Divisão de dados concluída: 70% treino, 15% validação, 15% teste.')
