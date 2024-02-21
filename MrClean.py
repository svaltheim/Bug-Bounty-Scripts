def remove_duplicate_domains(input_file, output_file):
    # Utilizar un conjunto para almacenar dominios únicos
    unique_domains = set()

    # Leer dominios del archivo de texto y eliminar duplicados
    with open(input_file, 'r') as file:
        for line in file:
            domain = line.strip()
            if domain:  # Saltar líneas en blanco
                unique_domains.add(domain)

    # Guardar los dominios únicos en un nuevo archivo
    with open(output_file, 'w') as file:
        file.write('\n'.join(unique_domains))

if __name__ == "__main__":
    input_file = input("Ingrese el nombre del archivo de entrada: ")
    output_file = input("Ingrese el nombre del archivo de salida para los dominios únicos: ")
    remove_duplicate_domains(input_file, output_file)
