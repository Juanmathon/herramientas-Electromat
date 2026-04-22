import os
import re

def update_logo():
    # Detect encoding and read base64 logo
    try:
        with open('base64_logo.txt', 'rb') as f:
            raw = f.read()
            # Handle potential UTF-16 BOM or UTF-8 BOM
            if raw.startswith(b'\xff\xfe'):
                data = raw.decode('utf-16').strip()
            elif raw.startswith(b'\xef\xbb\xbf'):
                data = raw.decode('utf-8-sig').strip()
            else:
                data = raw.decode('utf-8').strip()
        
        # Rigorous cleaning: remove any non-base64 leading characters (like hidden BOMs)
        import re
        data = re.sub(r'^[^\w\+/\=]+', '', data)
    except Exception as e:
        print(f"Error reading logo: {e}")
        return

    new_src = f"data:image/jpeg;base64,{data}"
    files = [
        'index.html',
        'Electromat_Generador_Ofertas.html',
        'Electromat_Transporte_Coste.html',
        'Electromat_Punto_X.html',
        'Electromat_Descuentos.html'
    ]

    for filename in files:
        if os.path.exists(filename):
            print(f"Updating {filename}...")
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace HTML src attribute
            content = re.sub(r'src="data:image/[^;]+;base64,[^"]+"', f'src="{new_src}"', content)
            
            # Replace JS constant
            content = re.sub(r'(const|var|let)\s+LOGO_BASE64\s*=\s*"[^"]+"', f'\\1 LOGO_BASE64 = "{new_src}"', content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Done updating {filename}")

if __name__ == "__main__":
    update_logo()
