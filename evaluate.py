"""Simple evaluation: translate sample sentences and compare with reference
translations by eye. Results are saved to evaluation_results.md.

Run with:  python evaluate.py
"""

from translator import TranslationError, translate

# (direction, input sentence, reference translation written by a human)
SAMPLES = [
    ("English → Spanish", "Break a leg at your interview tomorrow!",
     "¡Mucha suerte en tu entrevista mañana!"),
    ("English → Spanish", "It's raining cats and dogs.",
     "Está lloviendo a cántaros."),
    ("English → Spanish", "Could you please send me the report by Friday?",
     "¿Podría enviarme el informe antes del viernes, por favor?"),
    ("English → Spanish", "I'm feeling under the weather today.",
     "Hoy me siento mal."),
    ("Spanish → English", "Estoy muy emocionado por esta oportunidad.",
     "I'm very excited about this opportunity."),
    ("Spanish → English", "No tengo ni idea de lo que pasó.",
     "I have no idea what happened."),
    ("Spanish → English", "Ese examen fue pan comido.",
     "That exam was a piece of cake."),
    ("Spanish → English", "Nos vemos en la reunión, si Dios quiere.",
     "See you at the meeting, God willing."),
]


def main():
    lines = ["# Evaluation Results", ""]
    for i, (direction, source, reference) in enumerate(SAMPLES, start=1):
        try:
            output = translate(source, direction)
        except TranslationError as e:
            output = f"ERROR: {e}"
        print(f"{i}. [{direction}]\n   Input:     {source}\n   Model:     {output}\n   Reference: {reference}\n")
        lines += [
            f"### {i}. {direction}",
            f"- **Input:** {source}",
            f"- **Model output:** {output}",
            f"- **Reference:** {reference}",
            "- **Manual verdict:** (write: good / okay / needs prompt fix)",
            "",
        ]
    with open("evaluation_results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Saved to evaluation_results.md")


if __name__ == "__main__":
    main()
