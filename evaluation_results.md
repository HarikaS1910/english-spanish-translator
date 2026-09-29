# Evaluation Results

### 1. English → Spanish
- **Input:** Break a leg at your interview tomorrow!
- **Model output:** ¡Mucha suerte en tu entrevista mañana!
- **Reference:** ¡Mucha suerte en tu entrevista mañana!
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 2. English → Spanish
- **Input:** It's raining cats and dogs.
- **Model output:** Está lloviendo a cántaros.
- **Reference:** Está lloviendo a cántaros.
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 3. English → Spanish
- **Input:** Could you please send me the report by Friday?
- **Model output:** ¿Podría enviarme el informe para el viernes, por favor?
- **Reference:** ¿Podría enviarme el informe antes del viernes, por favor?
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 4. English → Spanish
- **Input:** I'm feeling under the weather today.
- **Model output:** Me siento mal hoy.
- **Reference:** Hoy me siento mal.
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 5. Spanish → English
- **Input:** Estoy muy emocionado por esta oportunidad.
- **Model output:** I am very excited about this opportunity.
- **Reference:** I'm very excited about this opportunity.
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 6. Spanish → English
- **Input:** No tengo ni idea de lo que pasó.
- **Model output:** I have no idea what happened.
- **Reference:** I have no idea what happened.
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 7. Spanish → English
- **Input:** Ese examen fue pan comido.
- **Model output:** That exam was a piece of cake.
- **Reference:** That exam was a piece of cake.
- **Manual verdict:** (write: good / okay / needs prompt fix)

### 8. Spanish → English
- **Input:** Nos vemos en la reunión, si Dios quiere.
- **Model output:** See you at the meeting, God willing.
- **Reference:** See you at the meeting, God willing.
- **Manual verdict:** (write: good / okay / needs prompt fix)


   ## Prompt iteration
   - Round 1: sentence 3 dropped "please" and used casual "tú" for a polite request.
   - Fix: added a rule to keep polite words and use "usted" for requests.
   - Round 2: sentence 3 now includes "por favor" and uses "Podría".