def resolver_codigo(problema):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Soluciona el siguiente problema de HTML/CSS sin explicación:\n{problema}\nSolo proporciona el código corregido.",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Ejemplo de uso:
problema = """
<div class="Photo"> 
            <div>
                <img src="Luis Risso Patron.jpg" alt="Foto de Perfil">      
            </div>           
        </div>
"""

solucion = resolver_codigo(problema)
print("Solución:", solucion)
