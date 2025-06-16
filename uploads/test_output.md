# Topic: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]

### Post #1 by **Anand S** (Course_faculty, faculty)
*January 14, 2025, 13:00 UTC*
Please post any questions related to [Graded Assignment 3 - Large Language Models](https://exam.sanand.workers.dev/tds-2025-01-ga3).

---

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. See below code for example

```
ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms

```

Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](https://discourse.onlinedegree.iitm.ac.in/c/docs-discourse/45)!

---

Deadline: Sunday, February 2, 2025 6:29 PM

[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@Saransh\_Saini](https://discourse.onlinedegree.iitm.ac.in/u/saransh_saini)

---

### Post #3 by **Nilay Chugh** (ds-students)
*January 15, 2025, 12:20 UTC*
how to get the dummy API key?

---

### Post #4 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 15, 2025, 14:59 UTC*
Hi Nilay,

In order to make a api call to openai chat completions you are required to send authentication information(openai key) in headers. For first question of GA3 you don’t have to send actual(working) api key, any dummy api key would work(you can put your name, or tds anything works)

kind regards

---

### Post #6 by **Nilay Chugh** (ds-students)
*January 18, 2025, 04:43 UTC*
which API should i use in 7th question

---

### Post #7 by **Guddu Kumar Mishra ** (ds-students)
*January 19, 2025, 07:36 UTC*
need help in question 4th. how can i correct this json body? sir [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Extract text from this image."
    },
    {
      "role": "user",
      "content": {
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}


```

error:The JSON body must have 1 message

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": {
        "text": "Extract text from this image.",
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}


```

Error: The message must have a 2 content parts

---

### Post #8 by **Guddu Kumar Mishra ** (ds-students)
*January 19, 2025, 16:53 UTC*
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) sir plz see it once.

---

### Post #9 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 21, 2025, 07:02 UTC*
Hi [@22f3001315](https://discourse.onlinedegree.iitm.ac.in/u/22f3001315) ,

You are almost correct, there are very minor changes that needs to be made.

Take help from Chat GPT or use this documentation which have correct json body [Vision - OpenAI API](https://platform.openai.com/docs/guides/vision).

Kind regards  
Jivraj

**Reactions:** ❤️ 1

---

### Post #10 by **Guddu Kumar Mishra ** (ds-students)
*January 21, 2025, 08:21 UTC*
it worked thanks sir

**Reactions:** ❤️ 2

---

### Post #12 by **Muhammed Adhil Pt** (ds-students)
*January 21, 2025, 11:25 UTC*
Are we supposed to buy open ai api key ?

---

### Post #13 by **Sakthivel S** (ds-students)
*January 21, 2025, 12:01 UTC*
No, if you scroll down to the last question, we can get our Ai Proxy key

---

### Post #14 by **Carlton D'Silva** (Regular, ds-students)
*January 21, 2025, 12:06 UTC*
[@nilaychugh](https://discourse.onlinedegree.iitm.ac.in/u/nilaychugh) [@22f3002034](https://discourse.onlinedegree.iitm.ac.in/u/22f3002034)

The API key is available at <https://aiproxy.sanand.workers.dev/>

The instructions on how to use the token is given at [GitHub - sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

You cannot use this token directly with Open AI or any other gpt. These are only valid via the API exposed by the above instructions.

You get a limit of $1. Use with care.

Kind regards

**Reactions:** ❤️ 2

---

### Post #15 by **Nilay Chugh** (ds-students)
*January 21, 2025, 14:30 UTC*
but the embedding model that is said to be used is text embedding 3 small, which is the model of OpenAI

---

### Post #16 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 22, 2025, 09:13 UTC*
Hi Nilay,

Yes you would need to use `text-embedding-3-small` model of openai for embedding questions.

Kind regards  
Jivraj

---

### Post #17 by **Nilay Chugh** (ds-students)
*January 23, 2025, 03:52 UTC*
i have a doubt, while submitting the GA3, both 7th and 8th questions require the API url to be active and connected right, but its not possible as both the URLs use same port, so if we check my 7th question URL is running right now, it’ll show as correct, but then if i run 8th question URL, the 7th question will automatically show the error, **is there any solution to this problem?**

**Reactions:** ❤️ 1

---

### Post #18 by **VIKASH PRASAD** (ds-students)
*January 23, 2025, 06:09 UTC*
Q5. How to handle the error ? sir [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

Error: The first input does not match the first text exactly

---

### Post #19 by **VIKASH PRASAD** (ds-students)
*January 23, 2025, 06:17 UTC*
Q4. How to handle this error? [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

```
{
  "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
  "object": "chat.completion",
  "created": 1737599182,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 592,
    "completion_tokens": 33,
    "total_tokens": 625,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.05490624000000001,
  "cost": 0.001974,
  "monthlyRequests": 14,
  "costError": "crypto.createHash is not a function"
}

```

Error: Model must be gpt-4o-mini

---

### Post #20 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 23, 2025, 10:58 UTC*
Hi Nilay,

nilaychugh:

> both the URLs use same port,

You can run two servers on different port numbers.

---

### Post #21 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 23, 2025, 11:05 UTC*
Hi Vikash,

I looked at your answers in backend. In answer you submitted response from openai, but you need to submit json object which is required for sending a request to LLM.

Kind regards

---

### Post #22 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 23, 2025, 11:07 UTC*
You made same mistake here, instead of response use json body that’s required for sending request to LLM.

Kind regards

---

### Post #23 by **VIKASH PRASAD** (ds-students)
*January 24, 2025, 01:17 UTC*
Q4. how to handle this error ? [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,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DOYQc83d7la67bar84q8XbP//qXbYYfS9YuJSdsaR+6nbLvsUsfWGWeU7n3vK93225du881L96Uvla4X6JP3+8X35P173KPeW77mwd12K92mm5bujW+sfVQ5+kX/ZNzvumvp+kXOanZa6KVeyqz8/cJ1UrfpuSOvvPLKK691+1rWM/UiPyLDokEPe1gp1752jYaJdvVOr/QOYhKV6x3UJDLXcGSlF9mld7aTiJBt38XSO9FJtEz02fa3yNdVrlLKXe5Sj9/YdhYNl6fImoi6yOed7lSjaragHaF46ENrNPl736vpeyFQeqc62SoXLRX9Ug/b7I78qIfomyi9yJ4ovnv2AmGSv8iX4yreEzkUlWcX+ftpK7t3ymdxm9vU4wei3yKM8h2D3dRZBE19+4VAudKV5j6cws6E6NxrXlMjbHe9a42GDukFwCTiLwpnO/+Rj6z2m4a9eqFUHve4GiV0nTqHsNIwLh05GY4P85D5qBfNk503O12i24udr0S8Rfnt8Pnc+DVOhuPctXZS+gXAJK37iNr3Yn0SDfe5a8whyvTyl9fovflDeey63fe+9ViOeUC+5gjjWEReOaVXN0d6+oXI5IiifO3APeQh9SiiHZ42j4q2mx/tNngtFrsadvfa/BlCCGHlsayintPYaqtSXvjCKlL9bbvYNjBnw7FxVqedVtOffnp1UEccUR3btttWB0hoNzgmDorod/SmHV0hwglbju/JTy7lEY+o29TuxcnJ2zEZIrhfzUxenKb3CFvHcjhc5eNELQo4T+WwnW3r3Ra1ow62vpVb3u5BuMuLo1W+612vlMMPr2W3pS5PL+J+ww3rVj+RrlzS7r9/KQ96UCkbbDBXyR5pLDIc/yEglHcM2/e22ZV1111XCYsx1IN9iZeddqr3bmdnm+0//ekqMHbeuQp/9T7wwCqGHvCAUp71rGpzP9lfWmW3SCF2iBcor8WLYwy77VbbcvvtSzn44LpAmsYC69BDa7r2evSj63GZ1j/mQ7scdVQVQO1aYu3446sAme4vjj886lHVbur8speVcthhdRFKgEE9LG4II/3KZyCKCCj97V73qvfae+9a91ZONhu7FmxicaiPKt+pp859MIdjF45GPP7xtW21i2MXjlYcdFA9EmI8WZgph7zYyZERotHRiPZyf+Vj95afoxePfeyq9w85ZLw9xrC4bNe213xt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u8WDcehevqFFP4N89S12sTg3P8h/DAsSbUzAa2NtpY+ab/R3/VAZlGVN5ivzhbpb7LKxvsuW7qeNzFe+KrKNafmbGyyEzQ36pHmEgCfS1U2ZlE1gwNgzBo1X+Rqn6ihw0fLV/7S7er3ylXWh6z35e1lUSMtGymtctP5rblAffYE9jTMP5hvr2mwabehBdu2hb3n+pbVHCCGEdc/6z+iZ+30R9J5zDeCEOCNb2y1SxBkMX8QTAeQnZzQNB+w6IpjAGDobwsJ1RI17EJTSi4o5KiE/ESwvQqaJT++7VnpOlMDg8OSvTMQgIShti5qrByEqL2mJGPcWfSNIiC9pOUjOVDpnpznT6Tq7H8HgGk6YEyUy50ur/mzkvsrN6fudIFUvkVR1mQ/p2cc95Dmd1t/qR0BZCBElykRsEBTqomzawAKC4PK58hNpIoUELQFMzItEawf3IrIJEW3CXkSUa7xEdC0MfO4lrfZodVdeUVR2bEK/CSeiSX6u0dZ+tnt6sZdrLQq0G7vJm4iRnl3dX1rl1fby8H4rp2vZTb2l0b6u97l+qAxso/8RWu5pgae9Wr8BMW4hpg677FLzcr2+wl7Ekn5EQOqbriWOjRll1j5NZLqXeiqrdmA35VGXVh79Vzptp96Qj/5i4el3+EwaaV2jTyuLhZI6EI3SKo/f3bONEfck+tlI2V3vxdbqp0+61qulN548N6HfqNOwLdm9oX3YktD2ub6u3Pog+zfkIW/9hG2kHYPd2YltXKMu+p1+RZy7lh3WdL5qc4Z2YBt1dQ/XmT/YZ1gvNvFSFnaSn3rpO+zo+jYvaW92kM41ymzMeVhXmZugl177yMtPZVEm5dMeFpDq4zN9zk+fqa+08tHX9Nv2z6XGBH1D2ZSTzZV92B4hhBDWLcsaqQ+zA4EpSuzbLU45pQovAp6wJ0LGFlzO4Ypc2zEQ+SMUnGUf23X5X8UCzy6Qc9QEn3+IRQgRRyGEEEIIS0VEfVgN0VPHPrxEAX0LjSiwiOE0jhE4AuIIgsikozSivqFGvD0E6Qy1o1L+dszDgieEEEIIYamJqA+r0b41gxh1BthZZed7HROaxvEIItU/9RGlF50fi+j/L+IM9xFH1HPRjo3sums9389OIYQQQghLTUR9GIW4d7beA4B+OkYyTTtfTtyH1fEQoqNJvlnEmWjnrJ0dDyGEEEJYDiLqQwghhBBCmHHyuF4IIYQQQggzTkR9CCGEEEIIM84aHr8JIYQQQgghrDQSqQ8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYaYp5f8A91ro9coVvFcAAAAASUVORK5CYII=" }
        }
      ]
    }
  ]
}

```

Error: The image\_url.url must be the base64 data URL of the image

---

### Post #24 by **VIKASH PRASAD** (ds-students)
*January 24, 2025, 02:02 UTC*
Q8. how to handle the error ? [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

<http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094>

{“name”: “expense\_balance”, “arguments”: “{“employee\_id”: 52094}”}

TypeError: Failed to fetch

---

### Post #25 by **Varad Rajadhyax ** (ds-students)
*January 24, 2025, 08:17 UTC*


> **Image Content:** *This screenshot shows the interface of an online data science course, likely an assignment or quiz.  Here's a breakdown of the key information:

**1. Assignment Details:**

* **Due Date:** Sunday, February 2nd, 2025, 11:59 PM IST.
* **Total Score:** 8.5 marks.
* **Current Score:** 2.75 marks.  The student has already saved their work multiple times.

**2. Recent Saves:**

The "Recent saves" section shows three instances where the student saved their work, all at 12:25:51 PM on January 24th, 2025. Each save resulted in a score of 2.75. This suggests the student may be iteratively working on the assignment, saving frequently to preserve their progress. The presence of a "Reload" button next to each save indicates the possibility of reverting to a previous saved state.

**3. Assignment Questions:**

The assignment consists of nine questions covering various aspects of Large Language Models (LLMs), including:

1. Sentiment analysis
2. Token cost estimation
3. Address generation
4. Computer vision applications
5. Embeddings generation and manipulation
6. Embedding similarity calculations
7. Vector databases
8. Function calling
9.  Prompt engineering to elicit a specific response ("Yes").

Each question has an associated mark value ranging from 0.75 marks to 1.5 marks.

**4.  Interface Elements:**

* **"Check" Button:**  Allows the student to check their answers and receive feedback.
* **"Save" Button:**  Saves the student's progress.

**5. Potential Issues/Observations:**

* The student's current score (2.75) suggests there is room for significant improvement.
* The multiple saves at the same timestamp might indicate an issue with the saving mechanism or the student repeatedly saving without making substantial changes.  Further investigation would be needed to confirm.


In summary, the screenshot provides a snapshot of a data science assignment focusing on LLM applications.  The student has made progress but still needs to complete the majority of the assignment. The interface is user-friendly and provides clear feedback on the student's progress.*



Why is my score is out of 8.5? It should be 9.5 right?  
It was 9.5 before a reload.

---

### Post #26 by **Sakthivel S** (ds-students)
*January 24, 2025, 08:37 UTC*
You should answer the third question every time the site reloads

**Reactions:** 👍 1

---

### Post #27 by **Varad Rajadhyax ** (ds-students)
*January 24, 2025, 10:06 UTC*


> **Image Content:** *This screenshot shows a data science course forum post presenting a coding challenge and the resulting error.

**The Challenge:**

The student is asked to write a Python function called `most_similar`. This function takes a dictionary called `embeddings` as input.  `embeddings` maps phrases (strings) to their vector representations (lists of numbers). The function should compute the cosine similarity between all pairs of these vector embeddings and return the pair of phrases with the highest cosine similarity as a tuple.

The provided `embeddings` dictionary contains one key-value pair:

```
embeddings = {"Packaging was excellent.": [-0.01674579456448555,-0.06481242924928665,-0.24050545692443848,0.042519159615039825,0.14857585728
```

**The Error:**

The student's attempt to solve the problem resulted in a `NameError`.  The complete error message is:

```
PythonError: Traceback (most recent call last): File "/lib/python312.zip/_pyodide/_base.py", line 523, in eval_code.run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File "/lib/python312.zip/_pyodide/_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "<exec>", line 5, in <module> NameError: name 'most_similar' is not defined
```

This indicates that the student did not define the function `most_similar` within their code.  The error is not related to the cosine similarity calculation itself (which the student has not attempted to code yet), only to the missing function definition.  The error traceback shows the error originating on line 5 of the student's code (which is not shown in the screenshot).*



For question no.6, there was some pre-written code there, right?  
I am not able to see it now.

---

### Post #28 by **Varad Rajadhyax ** (ds-students)
*January 24, 2025, 10:17 UTC*


> **Image Content:** *This screenshot shows a Python script execution in a Windows command prompt.  The user, Varad, is running a script named `request.py` located in  `C:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS`. The `-u` flag ensures unbuffered output.

The script execution resulted in an error, which is clearly displayed.  The error message is a JSON object indicating an OpenAI API quota exceeded error:


```json
{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
```

**Key Information:**

* **Error Type:** `insufficient_quota`  This indicates the user has reached their usage limit for the OpenAI API.
* **Error Message:** A clear message explaining the quota exceeded and directs the user to check their plan and billing. It also provides a link to OpenAI's API error documentation for further details.
* **OpenAI API Usage:** The script uses the OpenAI API, most likely for tasks like generating text, code, or translations.
* **User's Environment:** The user is working in a Windows environment and using Python.
* **Script Location:** The script is located in a temporary directory.  This is common practice during development.

**Expert Analysis:**

The user needs to upgrade their OpenAI plan or reduce their API usage to resolve this issue. The provided URL to OpenAI's documentation will help them troubleshoot and understand the different quota tiers available.  The `param` field being `None` suggests the error isn't tied to a specific parameter in the API request. The error is a general quota exhaustion.*



I am getting insufficient\_quota message for the 2nd question

---

### Post #29 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 27, 2025, 22:32 UTC*
21f3002277:

> The image\_url.url must be the base64 data URL of the image

I tried downloading image for your dataset it is 2.36 KB in size.  
Using base64 encoded string from `image_url.url` in your code when decoded comes out to be 8.18 KB, when I encoded image from your dataset and decoded it was 2.36 KB.  



> **Image Content:** *This screenshot shows a forum post from a data science course, likely dealing with image processing or data encoding.  The core information revolves around a Base64 encoded image.

**Key Information:**

* **Base64 Encoded Data:** The primary element is a long string of characters labeled "Base64*". This string represents a Base64 encoded PNG image.  The entire string is:

```
iVBORw0KGgoAAAANSUhEUgAAAVUAAABCCAYAAADXEilpAAAAAXNSROIArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADSMAAA7DAcdvqGQAACBJSURBVHhe7d0H1CxF2cbxQsw5YkZBQcWMAXNAEUxgAARFRUVBUVQEMSGiIqKAARUwo6JgzmIWDJhzzoo5B0wE++vf1Ba375zeZS/s3rvz+fzPmbO7M9XVVW+F96m3qmfX63pKCCGEEEIIYWY5z9zPEEIIIYQQwowSUR9CCCGEEMKME1EfQgghhBDCjBNRH0IIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjLNe1zP3+yJYb+5nCCGEEEIIYaWQSHOIIYQQQggzzrJH6v/731L+/vdSTjihlJ/9rJR//au+f8EL1rL11qVc85q1XPSi9b1p/v3vUn7961JOPLGUW9yil103LuX855/7sEden/98ff3nP6Vc8Yq1bL11KRe5SCnf+1YpJ50017Bno41KuelNS91ss7k35jjjjFL++MdS3vWuUn7/+/r3xS9eynWuU8od71DL2fCZ0nzsY6X861f1vbF6sKi0
```

* **Decoded Image Preview:** A yellow highlighted area shows a preview of the decoded image containing an email address: `21f3002277@ds.study.iitm.ac.in` and a number: `92893354`.

* **Image Metadata:**  The "File Info" section provides metadata about the decoded image:
    * Resolution: 757x66 pixels
    * MIME type: image/png
    * Extension: .png
    * Size: 8.18 KB
    * Download link: `image.png`
    * Bit depth: 8

* **Functionality:** The interface offers a button "Decode Base64 to Image" implying this is a tool to decode Base64 encoded images.  There's also a "Toggle Background Color" option, suggesting the ability to change the image background.


**Inferences:**

The email address and number in the decoded image suggest this is potentially a student ID or similar identifier within the context of the data science course.  The Base64 encoding and provided tools suggest a learning exercise or assignment related to image processing or data manipulation.*



Hints : check if encoding is correct.

---

### Post #30 by **Abhay Sharma** (ds-students)
*January 28, 2025, 04:11 UTC*
Is it required to give SCT for the ROE of this course?

Thank you.

---

### Post #31 by **Carlton D'Silva** (Regular, ds-students)
*January 28, 2025, 06:51 UTC*
SCT is not required for ROE. ROE is not proctored.

Kind regards

---

### Post #32 by **K Hari Prasath** (ds-students)
*January 28, 2025, 07:44 UTC*
This is regarding Question 2 I tried to find number of tokens for the message. Using chatgpt identified the followings are valid English words for the given text in the question **D** **m** **Ay** **E r u y Vy** **V Ky** **P** **c**. then, checked with <https://platform.openai.com/tokenizer>. whatever number given by it seems to wrong.  
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) could you inform me where I did mistake

---

### Post #33 by **Carlton D'Silva** (Regular, ds-students)
*January 28, 2025, 07:59 UTC*
[@23f2003853](https://discourse.onlinedegree.iitm.ac.in/u/23f2003853) You have to find the input tokens from the json response you receive from the proxy.

**Reactions:** ❤️ 1

---

### Post #34 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 28, 2025, 11:38 UTC*
Hi VIKASH,

This problem must be because CORS not enabled or you are running your application inside wsl, if you using WSL then you would need to identify ipaddress of WSL and use it in place of `127.0.0.1`

kind regards

---

### Post #35 by **K Hari Prasath** (ds-students)
*January 28, 2025, 11:48 UTC*
Sir, from where can I learn to locate the json response

---

### Post #36 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 28, 2025, 12:05 UTC*
Hi [@23f2003853](https://discourse.onlinedegree.iitm.ac.in/u/23f2003853) ,

You can learn from [Python’s Requests Library (Guide) – Real Python](https://realpython.com/python-requests/) tutorial about how to use requests module and see responses.

kind regards

---

### Post #37 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 28, 2025, 12:17 UTC*
22f3000445:

> I am getting insufficient\_quota message for the 2nd question

Which url are you using to send request to openai.

---

### Post #38 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 28, 2025, 12:20 UTC*
22f3000445:

> For question no.6, there was some pre-written code there, right?

pre-written code is not required for question 6.

---

### Post #39 by **Divyasree** (ds-students)
*January 28, 2025, 18:05 UTC*
In the 6th question ,as I open the graded assignment all the time the new question is generated (NUMERICAL DATA) and the previous answer shows as incorrect answer

My doubt is that should I again and again answer the same quetion(6) all the time until the due passes?  
Is there any alternative ways to look after this problem?

---

### Post #40 by **Saniya Naaz** (ds-students)
*January 29, 2025, 04:19 UTC*


> **Image Content:** *This screenshot shows a Python code snippet attempting to use the OpenAI API, likely for natural language processing.  The code sends a POST request to a URL (not shown) containing a JSON payload. The payload's `content` field specifies a task: identifying valid English words from a list of strings.

**Key Information:**

* **Purpose:** The code aims to filter out non-English words from a given list.  This suggests a potential application in text cleaning or data preprocessing.
* **API Interaction:** It uses the `requests` library to make a POST request to an API (likely OpenAI).  The `headers` and `data` variables (not fully visible) are assumed to contain necessary authentication and request details.
* **Error Handling:** The code includes error handling to check the HTTP status code of the API response.
* **Error Encountered:** The API request failed with a `429` status code, indicating that the request exceeded the current quota. The error message explicitly states "You exceeded your current quota". The error details, including the "insufficient_quota" code and type, provide context for the failure.
* **Debugging Information:** The `response.text` is printed to the console, revealing the full error response from the API. This is useful for debugging.
* **Code:** The relevant code is:

```python
response = requests.post(url, headers=headers, json=data)
# Check for successful response
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text) # Print the error response for debugging
```

**Conclusion:**

The code is functional but failed due to exceeding the OpenAI API's usage quota. The user needs to review their OpenAI account's usage limits and potentially upgrade their plan to resolve the issue.  The provided error message and link to OpenAI's documentation provide valuable clues for troubleshooting.*



how to solve???

---

### Post #41 by **Saniya Naaz** (ds-students)
*January 29, 2025, 04:49 UTC*
getting quota full message for 7th question. How to get the answers then?

---

### Post #42 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 29, 2025, 15:28 UTC*
Hi [@Divya1](https://discourse.onlinedegree.iitm.ac.in/u/divya1) ,

Question 6 requires to write a generic code for finding most similar pair. If your code is doing so, pls mention exact steps that you have used to arrive at answer.

---

### Post #43 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 29, 2025, 15:30 UTC*
[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

Are you using this document?

---

### Post #44 by **K Hari Prasath** (ds-students)
*January 30, 2025, 12:16 UTC*
each time when I run the following code it gives me different number. None of the answer is correct. can help to fix the issue  



> **Image Content:** *This screenshot shows Python code interacting with the OpenAI API's chat completions endpoint for GPT-4. Let's break down the key parts:


**1. API Interaction:**

* **`url = "https://api.openai.com/v1/chat/completions"`:** This line sets the URL for the OpenAI Chat Completion API.  Note that there is a typo in the screenshot ("apt" instead of "api").

* **`headers = {"Authorization": "Bearer (key)", "Content-Type": "application/json"}`:** This defines the headers for the API request.  Crucially,  `"Bearer (key)"` should be replaced with a valid OpenAI API key.

* **`data = {"model": "gpt-4", "messages": [{"role": "user", "content": user_message}]}`:** This constructs the JSON payload for the API request.  It specifies the model (`gpt-4`) and the user's message.  The `user_message` variable is not defined in the provided snippet.  The code also has a typo in `"robe"` which should probably be `"role"`.

* **`response = requests.post(url, headers=headers, json=data)`:** This sends a POST request to the API. It requires the `requests` library.

* **`response_json = response.json()`:** This parses the JSON response from the API.

**2. Error Handling and Token Usage:**

* **`if response.status_code != 200:`:** This checks if the request was successful (status code 200).

* **`print(f"Request failed with status code {response.status_code}: {response_json}")`:** This prints an error message if the request failed.

* **`input_tokens_used = response_json.get("usage", {}).get("total_tokens", "")`:** This extracts the number of tokens used from the API response. Note the nested `get` calls handle potential key errors gracefully.


**3. Data Preprocessing (Incomplete):**

* There's a section titled "List of input strings" and "List only the valid English words".  The code to actually perform this filtering is missing.  The listed words appear to be a test set for filtering out non-English words.

**4. Potential Issues:**

* **Missing Libraries:** The code implicitly uses the `requests` library.  This needs to be installed (`pip install requests`).
* **API Key:** The `(key)` placeholder needs to be replaced with a genuine OpenAI API key.
* **`user_message` Variable:** The code doesn't show how the `user_message` variable is defined or populated.
* **Typos:** There are several typos in the code (e.g., `"robe"`,  `"apt"`), which need to be corrected for it to function correctly.


In summary, the screenshot depicts a Python script designed to send user input to the OpenAI GPT-4 chat API, handle potential errors, and report the number of tokens consumed. However, the code is incomplete and contains several errors that need to be addressed before it runs properly.*



---

### Post #46 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 30, 2025, 21:04 UTC*
Hi [@23f2003853](https://discourse.onlinedegree.iitm.ac.in/u/23f2003853) ,

Please join tomorrow’s session, we can take it there, I am not sure why you facing this problem.

---

### Post #47 by **K Hari Prasath** (ds-students)
*January 31, 2025, 00:15 UTC*
Sure Sir. I am providing you the code below

```
import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",  
    "messages": [{"role": "user", "content": user_message}],  

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```
```

---

### Post #48 by **Shalini Saravanan** (ds-students)
*January 31, 2025, 09:20 UTC*
Hello Sir,

I am unable to recieve a proper output for q1 of ga3.  
This is my test message. Its been given in two lines.



> **Image Content:** *This screenshot shows a section of a data science course forum, likely displaying a list of usernames.  The format suggests a thread or post with several replies.

The top line, `2 b7 rksS94mn4`, seems to represent metadata.  "2" could be a numerical identifier (thread ID, post ID, or reply count). "b7" and "rksS94mn4" are likely usernames or unique identifiers associated with the original post or user.

The second line, `AM dNG4j EEvvk24Ev VEPi G LeeHS`, appears to be a list of usernames who have participated in the thread.  The  `G` username is highlighted, possibly indicating the current user or someone who made a significant contribution.

There is no code, commands, or error messages present in the screenshot. The information shown is purely textual, pertaining to user interactions within the forum.*



The below is my code for the question.

```
import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])

```

I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative

`user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"`

The error message i keep receiving is as below.



> **Image Content:** *This screenshot shows a code snippet and an error message from a data science course forum.  The code appears to be setting a `payload` variable, likely for an API request or similar interaction. The contents of the `payload` are obscured but the error message strongly suggests that it's related to a string or message field within the `payload`.

The crucial part is the error message:

`Error: The user message must be 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS, not 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS`

This indicates a problem with a "user message" field.  The error is perplexing because the expected value and the received value appear identical.  This points to several possibilities:

* **Hidden Differences:** There might be subtle differences not immediately apparent in the displayed strings, such as whitespace (leading/trailing spaces, tabs, non-breaking spaces), invisible characters, or encoding issues.
* **Case Sensitivity:** The comparison might be case-sensitive, although it looks unlikely given the visual match.
* **Data Type Mismatch:** The error could stem from an issue where the data type of the `user message` doesn't match what the system expects.  For instance, the system might require a specific encoding or a different data structure (e.g., an array instead of a string).
* **Bug:**  There's a possibility of a bug in the system performing the validation.

To troubleshoot, the student should:

1. **Inspect the `payload` variable more closely:**  The student needs to use debugging tools or printing techniques to reveal the complete `payload` and the exact value of the `user message` field, paying close attention to whitespace and characters that may not be visibly different.
2. **Check for encoding issues:** The encoding of the `user message` (e.g., UTF-8, ASCII) needs to be consistent throughout the system.
3. **Verify the data type:**  The code should ensure the `user message` is the correct data type expected by the system (and any related transformations done on the message).
4. **Examine the API documentation (if applicable):**  If the code is interacting with an external API, the documentation should specify the requirements for the `user message` format.


In summary, the error is highly unusual given the apparent duplication of the expected and actual values.  A thorough inspection of the `payload` contents and careful consideration of the points above are necessary for resolving this issue.*



Kindly advice on how to proceed.

Thanks and Regards  
Shalini

---

### Post #49 by **Carlton D'Silva** (Regular, ds-students)
*January 31, 2025, 09:37 UTC*
Hi Shalini,

Your `user_message` is incorrect. I looked at your exact GA and it works if you make sure your `user_message` is precisely what is given to you.

Hint: How do you store a multi-line variable in python?

Kind regards

**Reactions:** 👍 2

---

### Post #50 by **DIGVIJAYSINH SANDEEPSINH CHUDASAMA** (ds-students)
*January 31, 2025, 10:42 UTC*
Hello, could anyone please confirm that GA 3 is worth 9.5 points? Since our GAs are typically 10 marks apiece, I wanted to inquire about and obtain clarification on this.  
Thank you in advance.

---

### Post #51 by **Yogesh** (ds-students)
*January 31, 2025, 14:24 UTC*
I was unable to make the answer box in Question 3 visible. I was only able to make white space appear there, but couldn’t make it so that answer can be input to the box.

---

### Post #52 by **Carlton D'Silva** (Regular, ds-students)
*January 31, 2025, 14:40 UTC*
In addition to CSS classes there is also a tag attribute acting on it. Check carefully.

Kind regards

**Reactions:** 👍 1 ❤️ 1

---

### Post #53 by **Maheshwar Ture** (ds-students)
*January 31, 2025, 16:31 UTC*
I am getting below error for Q6 if i am importing sklearn libarary  



> **Image Content:** *This screenshot shows a `ModuleNotFoundError` in a Pyodide environment within a data science course forum.  A student is attempting to use the `scipy` library, but it's not installed despite being part of the Pyodide distribution.

The error message provides two solutions:

1. **Python solution:** `await micropip.install("scipy")`  This uses `micropip`, a package installer within Pyodide's Python environment, to install the `scipy` library.

2. **JavaScript solution:** `await pyodide.loadPackage("scipy")` This uses Pyodide's JavaScript API to load the `scipy` package.


The traceback indicates the error originated on line 4 of the executed code within the `<module>`.  The lengthy trace includes details from within the Pyodide library itself,  which are largely irrelevant to the core problem (missing `scipy`). The link provided, `https://pyodide.org/en/stable/usage/loading-packages.html`, points to Pyodide's documentation on package installation.

In summary, the student needs to use either the Python or JavaScript command provided to install the `scipy` package before their code will run correctly. The core issue is a simple missing package, not a deeper programming error.*



---

### Post #54 by **RAJ K BOOPATHI** (ds-students)
*February 01, 2025, 03:45 UTC*
Hi team, I am using OpenAI API key for solving Q7 and getting the error like below

```
{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

```

Is it necessary to pay for the OpenAI API key? Is there any other way?

**Reactions:** ❤️ 1

---

### Post #57 by **Carlton D'Silva** (Regular, ds-students)
*February 01, 2025, 05:38 UTC*
[@21f2000588](https://discourse.onlinedegree.iitm.ac.in/u/21f2000588)

Sure does add up to 9.5 , unless you want another question

Kind regards

**Reactions:** laughing 1

---

### Post #58 by **Anand S** (Course_faculty, faculty)
*February 01, 2025, 05:53 UTC*
Yeah, after all these years of learning and teaching computing, I realize I can’t even count to 10 correctly anymore.



> **Image Content:** *[Image description failed due to an API or network error]*



**Reactions:** laughing 4 ❤️ 1

---

### Post #59 by **RAJ K BOOPATHI** (ds-students)
*February 01, 2025, 05:55 UTC*
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) Please let me know if the code is needed for this. I can share the code generated by chatgpt

---

### Post #60 by **Wasim Ansari** (ds-students)
*February 01, 2025, 13:52 UTC*
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) , [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) Dear Sirs, I need help in solving this question. I have the same issue. I have tried tokenizer tool, tried writing request code but still couldn’t get the correct answer. I have tried numerous time and ended up consuming lot of tokens . What should be the optimal approach in this question?

```
  "id": "chatcmpl-Aw7eXQ8hciiQ0ZedatQEifFGxnLhQ",
  "object": "chat.completion",
  "created": 1738415805,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The valid English words from the given list are:\n\n- a\n- I\n- o\n- t\n- U\n- w\n- y\n- z",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 532,
    "completion_tokens": 34,
    "total_tokens": 566,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.01662212,
  "cost": 0.001863,
  "monthlyRequests": 41,
  "costError": "crypto.createHash is not a function"
}

```

---

### Post #62 by **Raunak Pugalia** (ds-students)
*February 02, 2025, 08:10 UTC*
Tried hundreds of different prompts, different situations but in Q9 AI is not responding “Yes”. Is there anything i am missing?

---

### Post #64 by **K Hari Prasath** (ds-students)
*February 02, 2025, 12:41 UTC*
Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code  
curl <https://api.openai.com/v1/chat/completions> \ > -H “Content-Type: application/json” \ > -H “Authorization: Bearer $TOKEN” \ '{ > -d ‘{ > “model”: “gpt-4o-mini”, "messa> “messages”: [{ > “role”: “user”, "c> “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ” > }] > }’ { “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”, “object”: “chat.completion”, “created”: 1738499426, “model”: “gpt-4o-mini-2024-07-18”, “choices”: [ { “index”: 0, “message”: { “role”: “assistant”, “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”, “refusal”: null }, “logprobs”: null, “finish\_reason”: “stop” } ], “usage”: { “prompt\_tokens”: 160, “completion\_tokens”: 53, “total\_tokens”: 213, “prompt\_tokens\_details”: { “cached\_tokens”: 0, “audio\_tokens”: 0 }, “completion\_tokens\_details”: { “reasoning\_tokens”: 0, “audio\_tokens”: 0, “accepted\_prediction\_tokens”: 0, “rejected\_prediction\_tokens”: 0 } }, “service\_tier”: “default”, “system\_fingerprint”: “fp\_72ed7ab54c” }

---

### Post #65 by **Vaishali** (ds-students)
*February 02, 2025, 15:38 UTC*
Pls give some kind of clue. It seems like a waste of so much time!

**Reactions:** ❤️ 1

---

### Post #67 by **Raunak Pugalia** (ds-students)
*February 02, 2025, 15:44 UTC*
i agree, i have wasted around 300 requests (prompts) and got nothing.

**Reactions:** ❤️ 1

---

### Post #69 by **VIKASH PRASAD** (ds-students)
*February 03, 2025, 06:54 UTC*
Sir I am stuck in Q4. how to handle the error please help me [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)

Error: The image\_url.url must be the base64 data URL of the image

---

### Post #70 by **DIGVIJAYSINH SANDEEPSINH CHUDASAMA** (ds-students)
*February 03, 2025, 07:22 UTC*
Okay thank you sir, for the clarification.

---

### Post #71 by **Yogesh** (ds-students)
*February 03, 2025, 14:11 UTC*
You have to download that image, and find the base\_url of that image.

---

### Post #72 by **VIKASH PRASAD** (ds-students)
*February 03, 2025, 14:22 UTC*
from where to download

---

### Post #73 by **Yogesh** (ds-students)
*February 03, 2025, 15:09 UTC*
The image is part of the question.

**Reactions:** 👍 1

---

### Post #74 by **Anand S** (Course_faculty, faculty)
*February 03, 2025, 15:28 UTC*
For those who want to experiment with GPT-4o Mini (or other models), [Github Models](https://github.com/marketplace/models) is free. You can explore and compare models, including GPT-4o Mini, DeepSeek R1, and others.

It has rate limits, so you can’t use it in production, but is a good place to prototype applications and experiment with prompts.

Please let me know if you face any problems accessing it.

**Reactions:** ❤️ 2

---

### Post #75 by **Dwarakesh** (ds-students)
*February 03, 2025, 18:25 UTC*
how to answer the question in first place ?

---

### Post #76 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 03, 2025, 22:07 UTC*
Check if you are requesting through anand sir’s proxy [AI Proxy](https://aiproxy.sanand.workers.dev/).

---

### Post #77 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 03, 2025, 22:10 UTC*
sklearn might be using scipy for some purpose, just install it, it should work.

Btw what are you trying to do with Sklearn?

---

### Post #78 by **Maheshwar Ture** (ds-students)
*February 04, 2025, 03:13 UTC*
thanks for the reply i was using cosine function but got another solution.

---

### Post #80 by **Naga durga prasad E** (ds-students)
*February 04, 2025, 09:51 UTC*
Q2 LLM Token Cost ,

We have <https://platform.openai.com/tokenizer> , which helps us count tokens in a string, shouldn’t this be a better way than calling the API? However the returned value does not show as correct answer!

---

### Post #81 by **Tanmay Garg** (ds-students)
*February 04, 2025, 13:27 UTC*
Hi guys, just wanted to share that I found it hysterical when I saw this question:  



> **Image Content:** *This screenshot shows a graded assignment from a data science course on the OpenAI API.  The student is tasked with constructing a JSON body for an OpenAI chat completion API call to generate 10 fake but plausible US addresses.

The key requirements are:

* **API call:** The request must be made to `https://api.openai.com/v1/chat/completions`.
* **Model:** Use the `gpt-40-mini` model.
* **System message:** `"Respond in JSON"`
* **User message:** `"Generate 10 random addresses in the US"`
* **Structured outputs:** The response must be a JSON array of objects. Each object must have the following `required` fields:  `"apartment"` (string), `"zip"` (number), `"latitude"` (number).
* **`additionalProperties`:** Must be set to `false` to prevent unexpected fields in the response.

The assignment emphasizes that the student should *not* run the API call; the goal is to write the correct JSON body only.  The interface shows a partial JSON schema example with warnings about missing `required` fields and the importance of setting `additionalProperties` to `false`. The score indicator shows the student has only achieved 1 out of 9.5 points.  The presence of an "Activate Windows" watermark suggests the student is working on a non-activated version of Windows.*



  
Like I literally showed this question to my mother and younger bro, stating the fact we ourselves had enable the answer box, they laughed there pants off…  
More courses could be like this.

---

### Post #82 by **Andrew David** (ds-students)
*February 04, 2025, 13:59 UTC*
**Q4**  
s3 string was given by

```
image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"

```

  
s4 string given by :   

used this [link](https://www.base64-image.de/)  to generate image url  
  
 Then checked them both, they were the same

```
for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)

```

i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?  
I know i’m missing something, but why?

---

### Post #83 by **Andrew David** (ds-students)
*February 04, 2025, 14:05 UTC*


> **Image Content:** *This screenshot shows a student's attempt at solving a coding problem within a data science course forum.  The problem requires writing a Python function `most_similar(embeddings)` that computes the cosine similarity between all pairs of embeddings and returns the pair with the highest similarity as a tuple.

**Key Information:**

* **Problem Statement:** The student needs to write a Python function that takes a list of embeddings (likely numerical vectors representing text phrases) as input.  It should calculate the cosine similarity between each pair of embeddings and identify the pair with the maximum similarity. The function should then return a tuple containing the corresponding phrases (not shown in the provided embeddings input).

* **Student's Code:** The student's incomplete code is:

```python
import numpy

def most_similar(embeddings):
    # Your code here
    return (phrase1, phrase2)
```

* **Error Message:** The code results in a `NameError: name 'phrase1' is not defined`. This error clearly indicates that the variables `phrase1` and `phrase2` are used in the `return` statement without being defined earlier in the function.  The student has not implemented the core logic to calculate cosine similarities and map them back to the original phrases.

* **Missing Logic:** The crucial part—calculating cosine similarities using `numpy` (which was imported correctly) and finding the indices corresponding to the highest similarity—is missing. The student hasn't written the code to compute cosine similarity using `numpy.dot` and `numpy.linalg.norm`, and they haven't linked the numerical results back to the original phrases associated with the embeddings.

**Expert Analysis:**

The student demonstrates a basic understanding of function definition and the `numpy` library. However, they have failed to implement the algorithmic core of the problem.  They need to:

1. **Iterate Through Embeddings:** Use nested loops or vectorized operations (preferred for efficiency with `numpy`) to calculate the cosine similarity between each pair of embeddings.

2. **Cosine Similarity Calculation:**  Calculate the cosine similarity using `numpy.dot` for the dot product and `numpy.linalg.norm` for the vector magnitudes. The formula is: `cos_sim = numpy.dot(a, b) / (numpy.linalg.norm(a) * numpy.linalg.norm(b))`.

3. **Track Maximum Similarity and Indices:** Keep track of the highest cosine similarity found and the indices of the corresponding embeddings.

4. **Map Indices to Phrases:**  The problem statement implies that the embeddings are associated with phrases (not directly visible in the screenshot).  The student must have access to this mapping (e.g., a list or dictionary) to retrieve the correct phrases to return in the tuple.


In short, the student's attempt is severely incomplete and lacks the essential calculations and data handling required to solve the problem. The `NameError` is simply a symptom of the much larger issue of missing core implementation.*



---

### Post #84 by **PalakAnand** (ds-students)
*February 04, 2025, 14:05 UTC*


> **Image Content:** *This screenshot shows a student's response in a data science course forum, likely related to an API interaction exercise.

**Key Information:**

* **Task:** The student is asked to provide the API URL endpoint for their implementation.  The expected format is shown as `http://127.0.0.1:8000/execute`.
* **Student Response:** The student provided `http://127.0.0.1:8000/execute`, which matches the example.
* **Error:**  The system indicates a `SyntaxError: "undefined" is not valid JSON`. This error implies the API response is not valid JSON, which is crucial for data processing. The cause of the error isn't directly shown in the screenshot but is likely related to a problem with the data sent to the API or how the API is configured.
* **Debugging Guidance:** The following explanation assists the student in debugging.  The system will make a GET request to the provided URL with `?q=...`, where `...` represents the task. This will be compared to an expected response to verify correctness. The order of arguments in the query (`?q=...`) should match the function definition used to generate the task. This suggests the student should inspect their request,  how their task data is formatted, and the API response for inconsistencies.


**Code/Commands:**

There is no code in the sense of a programming language directly shown. The key element is the URL:

`http://127.0.0.1:8000/execute`

**Error Message:**

`SyntaxError: "undefined" is not valid JSON`


**Expert Analysis:**

The student correctly identified the API endpoint. The `SyntaxError` indicates a problem not with the endpoint itself but with the data being sent or received by the API.  The student should check the structure of their request, ensuring the `?q` parameter contains correctly formatted JSON data representing the task. They should also examine the API response, particularly if the response doesn't match the expected format or is missing expected fields (hence the "undefined"). The error highlights a common issue in API interactions—data serialization (JSON encoding/decoding).*



  
This is in context to Q8. This is a screenshot of the response I am getting when i run the same API on my FastAPI/docs response page, it gives the correct response. But when I check it on the assignment page i get the following error. If you would like to know the code, pls let me know. [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

---

### Post #85 by **Sudhish Narayan S** (ds-students)
*February 04, 2025, 16:16 UTC*
Good Evening, I have a doubt regarding 7th and 8th question. I am getting this error of expecting three matches while saving. But, Externally when I check this API, I tried considerable test cases, and I am getting the output correctly. Can you please check this and give a solution. Thank You  


> **Image Content:** *The screenshot shows a Python dictionary.  The dictionary has a single key-value pair:

* **Key:** `'matches'`
* **Value:** A Python list containing three strings: `'banana'`, `'watermelon'`, and `'jamaica'`.

This data structure suggests that the code snippet likely resulted from a search or matching operation where the three strings were identified as matches.  The context within the data science course forum would need to be considered for a more precise interpretation.  However, without further context,  we can only infer that the output represents a successful search result for the three fruits.*

  



> **Image Content:** *This screenshot shows a question and answer from a data science course forum, likely related to a backend API development assignment.

**Key Information:**

* **The core issue:** A student is encountering an error ("Error: Expected 3 matches") likely stemming from an API request to a similarity endpoint.  The error message suggests the API response did not return the expected number of matches (3).
* **CORS Configuration:**  The instructor advises the student to check their Cross-Origin Resource Sharing (CORS) configuration. The student needs to ensure their API server allows `OPTIONS` and `POST` requests from any origin ("all origins") and includes all headers in the response.  This is a common problem when making API requests from a client (like a web browser or a front-end application) that is hosted on a different domain than the API server.
* **API Endpoint:** The expected format of the API endpoint URL is provided as an example: `http://127.0.0.1:8000/similarity`. This indicates a local development environment (using the localhost address `127.0.0.1` on port 8000) and a specific endpoint named `/similarity` for retrieving similarity information.  The student has correctly provided this endpoint in their answer.


**Code/Commands:**

The only code snippet present is the API URL endpoint:

`http://127.0.0.1:8000/similarity`

**Error Message:**

`Error: Expected 3 matches`  This error message is not a programming language error, but rather a custom error message from the API itself. It indicates that the API returned fewer results than anticipated.  The likely cause is a problem with the data or the logic that generates similarity matches within the API.*



---

### Post #86 by **Sudhish Narayan S** (ds-students)
*February 04, 2025, 17:52 UTC*
This is regarding the 8th question. Same here, I am getting the answer for all the test cases, but then also, I am getting error in the portal while saving. Please help me out here. Thank You.  



> **Image Content:** *This screenshot shows a forum post from a data science course, likely involving a web application or API interaction.  Let's break down the key information:

**1. URL:**

`127.0.0.1:8001/execute/?q="Calculate%20performance%20bonus%20for%20employee%2010056%20for%202025."`

This is a URL likely pointing to a local development server (indicated by `127.0.0.1`). The `/execute/` path suggests a functionality to execute a specific task or query. The `q` parameter contains a URL-encoded query string, requesting calculation of a performance bonus for employee ID 10056 in the year 2025.  The `%20` represents spaces.


**2. JSON Data:**

```json
{"name":"calculate_performance_bonus", "arguments":"{\"employee_id\": 10056, \"current_year\": 2025}"}
```

This is a JSON (JavaScript Object Notation) object.  It appears to be a structured representation of the request sent to the server.

* `"name":"calculate_performance_bonus"`:  This is the name of the function or endpoint being called.

* `"arguments":"{\"employee_id\": 10056, \"current_year\": 2025}"`: This contains the arguments for the function. Note the nested double quotes.  The inner JSON `{"employee_id": 10056, "current_year": 2025}`  provides the employee ID (10056) and the year (2025) as input parameters to the `calculate_performance_bonus` function.

**Potential Issues:**

The most noticeable issue is the double-quoting of the `arguments` field. The `arguments` value should contain a JSON object directly. The current format is incorrect and likely causing a problem in how the server interprets the request.  The server likely expects:

```json
{"name":"calculate_performance_bonus", "arguments":{"employee_id": 10056, "current_year": 2025}}
```

The student might need to review how to properly format JSON objects within their application's data exchange.  The URL encoding in the first part further underscores the potential confusion between string formatting within the application and URL encoding in the request.  This is a common mistake for beginners.*



  



> **Image Content:** *This screenshot shows a question and answer from a data science course forum.  A student is asking for the correct API URL endpoint.

The instructor provides an example: `http://127.0.0.1:8000/execute`

The student then provides their attempted URL: `http://127.0.0.1:8001/execute`

Crucially, the student receives the error message: `TypeError: Failed to fetch`. This indicates that the code attempting to access the API at the provided URL (`http://127.0.0.1:8001/execute`) failed.  The likely cause is that either the API is not running on port 8001, or there's a problem with the student's network configuration or code that prevents reaching the server.  The difference between the example and the student's URL (port 8000 vs 8001) suggests a simple configuration error.  Further investigation is needed to resolve the issue.*



**Reactions:** 👍 1

---

### Post #87 by **Jayaram** (ds-students)
*February 04, 2025, 18:07 UTC*
For question 1 getting the below response … not sure what it means  
ythonError: Traceback (most recent call last): File “/lib/python312.zip/\_pyodide/\_base.py”, line 523, in eval\_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File “/lib/python312.zip/\_pyodide/\_base.py”, line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File “”, line 53, in TypeError: unhashable type: ‘dict’

---

### Post #88 by **Jayaram** (ds-students)
*February 05, 2025, 01:44 UTC*
[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)  
for question 2 what does the below instruction mean … also how to indicate this in a prompt ’ Remember: indicating that this is a `user` message takes up a few extra tokens. You actually need to make the request to get the answer."

---

### Post #89 by **Jayaram** (ds-students)
*February 05, 2025, 03:57 UTC*
For token count query , trying to do something like below any issues with this

```
import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""       
    SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz   
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for  a message lile below. Try excluding tokens used for understanding this prompt"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)

```

---

### Post #90 by **Naman Gupta** (ds-students)
*February 05, 2025, 07:08 UTC*
I GOT THE CORRECT ANSWER F0R QUES 7 & 8 STILL MY SCORE IS SHOWING 8 DOES ANYONE KNOW HOW TO DO THIS ?  



> **Image Content:** *This screenshot shows instructions for a data science course exam (TDS 2025 Jan GA3) focusing on Large Language Models.  The key information is:

* **Exam Title:** TDS 2025 Jan GA3 - Large Language Models
* **Assessment Type:**  An exam involving running multiple servers simultaneously.
* **Instructions Summary:**  Students are allowed to use any resources (internet, ChatGPT, etc.), libraries, and frameworks. They can check their answers multiple times using the "Check" button and save their work using the "Save" button.  The final saved submission will be graded.  The exam is designed to be "hackable," meaning students are allowed to manipulate the code to find answers.  Browser issues are acknowledged, and solutions (disabling security restrictions or using a different browser) are provided.  The system saves answers client-side (in the browser) not server-side.

**Specific actions highlighted:**

* **`Check`**: A button to check answers.  Multiple checks are permitted.
* **`Save`**: A button to save answers. Multiple saves are permitted, with only the last save being graded.


The instructions emphasize a flexible and open approach to the exam, encouraging students to leverage all available resources and even explore the codebase to find solutions. The note about multiple servers indicates a more complex setup than a typical online quiz.  The link to Discourse suggests a forum for clarifying any questions.*



---

### Post #91 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 05, 2025, 10:25 UTC*
Use addition : to add up your score for each question.  
eq:  
1+ 1 = 2  
Fractions are harder  
1.5 + 1 = 2.5



> **Image Content:** *This screenshot shows a list of questions for a data science course assignment or quiz, specifically focusing on Large Language Models (LLMs).  The questions cover various aspects of LLM application and functionality, each with a specified point value.

Here's a breakdown:

The assessment seems to be heavily focused on practical application of LLMs, covering tasks such as:

* **Sentiment Analysis:**  Analyzing the emotional tone of text using an LLM.
* **Token Cost:** Understanding the pricing and resource consumption associated with using LLMs (based on tokens processed).
* **Address Generation:** Using LLMs to generate addresses, highlighting their potential in data entry or similar tasks.
* **LLM Vision:** Applying LLMs to image-related tasks (the specifics are not detailed in this screenshot).
* **Embeddings:** Working with and understanding vector embeddings generated by LLMs, a common technique in semantic similarity tasks.
* **Embedding Similarity:** Measuring the similarity between different embeddings.
* **Vector Databases:**  Utilizing vector databases which are often used in conjunction with LLMs and embeddings for efficient similarity search.
* **Function Calling:**  Leveraging the function calling capabilities of LLMs, a more advanced technique.
* **Simple Prompt Engineering:**  Getting a specific, simple response ("Yes") from an LLM, demonstrating basic prompt design.


The point values suggest a relatively short assignment or quiz, with some questions carrying slightly more weight than others (Vector Databases and Function Calling are weighted at 1.5 marks).  There is no code or error message present in this screenshot.*



**Reactions:** ❤️ 1

---

### Post #92 by **Tanmay Garg** (ds-students)
*February 05, 2025, 10:27 UTC*
To this question I have checked values ranging from 6 to 13 none of them are correct, using openAI Tokenizer online tool.  



> **Image Content:** *This screenshot shows a student working on a data science exam question within a web-based learning environment.  The question concerns estimating the number of tokens used by OpenAI's GPT-40-Mini when processing a specific user prompt.

**Key Information:**

* **Course:** The URL indicates this is an exam (`exam.sanand.workers.dev/tds-2025-01-ga3`) for a course likely titled "TDS 2025 Jan," potentially a data science course.
* **Question:** The core task is to determine the number of tokens used by GPT-40-Mini for a user prompt. The student needs to input a number representing the token count in the designated field.  The question explicitly states that the method of indicating the input is a user message takes up extra tokens.  The student must actually make the request to get an accurate answer.
* **Context:** The question provides context about LexiSolve Inc., a company using OpenAI's language models.  The importance of accurate token accounting for cost optimization is emphasized.  The internal diagnostic tool is only mentioned to set context. It isn't directly used to solve the problem.
* **User Input:** The student needs to input the number of tokens used by the model, which requires running the specified prompt against the OpenAI API.


**Code/Commands/Error Messages:**

There is no code, commands, or error messages visible in the screenshot, only the text prompt:

`list only the valid English words from these:`

This is a prompt for the user to provide to OpenAI's GPT-40-Mini. The missing portion of the prompt is obscured in the screenshot. The obscured text should contain the text whose tokens need to be counted.

**Overall Assessment:**

The screenshot captures a moment where a student is faced with a practical application of tokenization, a fundamental concept in natural language processing. Successfully answering this question involves not only understanding tokenization but also having the practical experience of using OpenAI's API.  The answer cannot be determined directly from the screenshot. The student needs to interact with the OpenAI API to get the correct number of tokens.*



  



> **Image Content:** *This screenshot shows a web page from `platform.openai.com/tokenizer`, likely part of an OpenAI data science course.  The user is exploring a tokenizer, a tool that breaks down text into individual units (tokens).

**Key Information:**

* **Tokenizer functionality:** The webpage demonstrates how the tokenizer processes text.  The input box is currently empty, but the example shows that "List only the valid English words from these:" is tokenized into 10 tokens and 47 characters.
* **Token-to-character ratio:**  The page explains that a helpful rule of thumb is one token corresponds to roughly 4 characters of common English text, or about ¾ of a word.  (100 tokens ≈ 75 words).
* **Available packages:**  The page recommends the `tiktoken` package for Python and the community-supported `@dbdq/tiktoken` package for JavaScript for programmatic tokenization.

**Code/Commands:**

There is no executable code in the screenshot. The highlighted text  `"list only the valid English words from these:"` is the input text to the tokenizer, not code.


**Error Messages:**

There are no error messages visible in the screenshot.

**Overall:**

The screenshot captures a user's interaction with a text tokenizer provided by OpenAI. The focus seems to be on understanding the relationship between tokens, characters, and words in text processing, and learning about available toolkits for programmatic text tokenization.*



  
Please help me were I am going wrong.

---

### Post #93 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 05, 2025, 10:29 UTC*
22f3002723:

> `user` message

that means it should be a user message

```
messages = [
{
"role":"user",
"content":"message"
}
]

```

---

### Post #94 by **Tanmay Garg** (ds-students)
*February 05, 2025, 10:51 UTC*
Keep getting this error.  



> **Image Content:** *This screenshot shows a student working on a data science course exam.  The exam question involves interacting with a similarity API endpoint.

**Key Information:**

* **Task:** The student needs to identify the correct API endpoint and send a POST request with a JSON body containing "docs" and "query" data.  The API is designed to return similarity matches between documents.

* **API Endpoint:** The provided URL is `http://127.0.0.1:8000/similarity`.  This is a local development endpoint, suggesting the student is working on a local server.

* **Error Message:** The student has received an error: `"Error: Got incorrect matches: Our customer feedback survey revealed that ease of use is a key area for improvement., The infrastructure upgrade includes improvements in data storage and retrieval., The technical documentation for the new product line is now available online."` This indicates that the API response is not what is expected. The error message itself is unexpected and seems to be returning general feedback instead of an error related to the request.

* **CORS Configuration:**  The instructions emphasize enabling CORS (Cross-Origin Resource Sharing) to allow `OPTIONS` and `POST` requests, possibly from any origin. This is a common requirement for web APIs that need to be accessed from different domains.

* **Expected Response:** A JSON response similar to `{"matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]}` is anticipated, showcasing a ranked list of matching documents.

* **Current Score:** The student's current score is 0 out of 9.5.

* **Function Calling Section:** The bottom of the screenshot introduces a separate section about "Function Calling with OpenAI," suggesting the course also covers interacting with large language models (LLMs) like those from OpenAI to generate structured function calls.


**Code/Commands:**

No explicit code is visible in the screenshot beyond the URL  `http://127.0.0.1:8000/similarity` which is the API endpoint. The student will need to write code to make the POST request. The error message shows that the API is not working as expected and is delivering feedback rather than the intended similarity matches.*



---

### Post #95 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 05, 2025, 10:57 UTC*
Try sending an api call to openai.

---

### Post #96 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 05, 2025, 11:09 UTC*
Check with network tab, you would see the response of api call being made, Compare that with expected output.

Regrading question 8, you would need to check if cors are enabled, check in browser console tab for more.



> **Image Content:** *This screenshot shows a student using their browser's developer tools (specifically the Network tab) to inspect network requests made by a web application, likely part of an online data science course.  The key information is:

1. **Two identical requests:** The Network tab displays two identical requests, both labeled `1.0?cors=true&content-type=application/x-json-stre...6V%3D4%26LU...`.  The ellipsis (...) indicates a truncated URL. The `cors=true` parameter suggests the requests are handling Cross-Origin Resource Sharing (CORS) correctly.  The `content-type=application/x-json-stre` indicates the expected response is JSON data.  The unusual characters after the ellipsis are URL-encoded.  Without the full URL, it's impossible to determine the exact endpoint.


2. **Successful Response:** The "Response" column shows a JSON response: `{"acc":1,"webResult":{}}`. This suggests a successful API call where `acc` is likely an access code (value 1) and `webResult` is an empty object. This empty object could indicate that there's no other data to return.


3. **Timing:** The timing information in the Network tab shows that each request took roughly between 8000 and 10000 milliseconds.  This indicates a relatively slow response time.  This warrants further investigation into the cause.


4. **Context:** The browser's tabs and bookmarks suggest the user is working on a data science course involving a Titanic dataset from Academia.edu, and possibly has other related assignments from IIT Madras. This provides the context for the web requests.

**Potential Issues and Further Investigation:**

* **Slow Response Time:** The 8-10 second response time could be due to server-side issues, network latency, or inefficiencies in the application's API. This should be reported.
* **Truncated URL:** The truncated URL prevents full analysis of the API endpoint. The full URL is crucial in identifying potential problems.
* **Empty `webResult`:**  The empty `webResult` in the JSON response warrants further examination. It's possible this is expected behavior, but it might also indicate a bug or missing data.

In summary, the screenshot depicts a student debugging or investigating a web application used in their data science course.  The slow response time and the need to view the full URL should be addressed.*



---

### Post #97 by **Yogaswetha** (ds-students)
*February 05, 2025, 11:09 UTC*
i am unable to find the answer box plss guide me through that

---

### Post #99 by **Tanmay Garg** (ds-students)
*February 05, 2025, 11:11 UTC*
You could use AI assistance it helped me.  



> **Image Content:** *This screenshot shows a student ("22f2001630") posting on a data science course forum's discussion thread about an error they are encountering.  The post includes a screenshot of the error itself, which is partially obscured and unreadable.  The post's ID is "22f2001630", and the timestamp indicates it was posted 18 minutes prior to the screenshot.  A reply ("23f2000098") suggests the student ask for AI assistance.

The student has opened their browser's developer tools, specifically the "Elements" and "Styles" panels. The "Elements" panel displays the HTML source code of the webpage, showing a `<body>` tag with several classes relevant to the forum's structure and the current page (e.g., `primary-group-ds-students`, `chat-enabled`, various category and tag identifiers).  There are also included scripts from `discourse-cdn.com`. The "Styles" panel shows the CSS styles applied to the `<body>` element, including `background-attachment: fixed;`, `background-size: cover;`, `min-height: 100%;`, and `box-sizing: border-box;`.  This information suggests a problem with the forum's frontend rendering.

The bottom right corner shows a Windows activation prompt. The "How can I help you?" AI assistance box indicates an experimental AI feature is in use within the browser's developer tools. This experimental feature can access webpage data via Web APIs and send it to Google for analysis to improve performance.*



---

### Post #100 by **Sudhish Narayan S** (ds-students)
*February 05, 2025, 11:12 UTC*
Oh OK sure. I will try out and let you know. Thank You!

---

### Post #102 by **Tanmay Garg** (ds-students)
*February 05, 2025, 11:26 UTC*
Got the answer but it was wired that I had run the curl command three time and the 3 times I got different result.

---

### Post #103 by **Yogaswetha** (ds-students)
*February 05, 2025, 11:28 UTC*
its not working for me any other options plss??

---

### Post #104 by **Aashutosh** (ds-students)
*February 05, 2025, 12:51 UTC*
23f2003853:

> rm me where I did mistake

Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results. Any help would be appreciated.  



> **Image Content:** *This screenshot shows a section of a data science course forum or online assignment interface.  The user is being asked to provide the API URL endpoint for their implementation of a task.

**Key Information:**

* **CORS Requirement:** The system explicitly states that Cross-Origin Resource Sharing (CORS) must be enabled to allow GET requests from any origin. This is crucial for allowing external requests to access the API.

* **API Endpoint Input:** The user is expected to enter the API URL endpoint in the provided input field.  An example is given: `http://127.0.0.1:8000/execute`.  The user has entered `http://127.0.0.1:8001/execute`.

* **Error Message:** A `TypeError: Load failed` error is displayed, indicating that the API call failed to load, likely due to issues with the provided URL or the API itself. The error suggests a problem either with the user's API implementation or network connectivity.

* **Testing Methodology:** The system explains how it will test the provided endpoint. It will send a GET request to the specified URL with a query parameter `?q=...` containing a task, and verify if the response matches the expected output. The order of arguments in the request must match the function definition.


**Code/Commands:**

The user's input: `http://127.0.0.1:8001/execute`

**Error:**

`TypeError: Load failed`


**Analysis:**

The error likely stems from the user's API endpoint `http://127.0.0.1:8001/execute`.  Possible reasons include:

* **Incorrect Port:** The port `8001` might be incorrect. The server may be running on a different port.
* **Server Not Running:** The API server might not be running on the specified IP address and port.
* **CORS Misconfiguration:** Despite the instruction, CORS might not be correctly configured on the server, preventing the GET request from succeeding.
* **Network Issues:** Network problems could prevent the system from reaching the API.
* **API Implementation Error:**  The user's API implementation might have a bug that causes it to fail.

The user needs to debug their API implementation and ensure it's correctly running and configured to handle GET requests, including appropriate CORS headers.  They should double-check the server's port and ensure network connectivity is established.*



```
curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}

```

---

### Post #105 by **Abhigyan Das** (ds-students)
*February 05, 2025, 13:56 UTC*
For question 2, do we have to make the API call to the proxy or openai? If to the proxy, are there any instructions on the page *before* question 2 that would have pointed me in that direction?

---

### Post #106 by **Yogaswetha** (ds-students)
*February 05, 2025, 14:04 UTC*


> **Image Content:** *This screenshot shows a student working on a data science course assignment involving API interaction.  Let's break down the key information:

**1. The Task:** The student needs to build an API endpoint that accepts a ticket ID and returns its status.  The provided JSON snippet defines the expected API function:

```json
{
  "name": "get_ticket_status",
  "arguments": "{\"ticket_id\": 83742}"
}
```

**2. API Endpoint:** The student has entered the API URL `http://127.0.0.1:8000/execute` which appears to be a locally hosted server.

**3. Error:** The system is reporting a `SyntaxError: "undefined" is not valid JSON`. This indicates the API is not returning valid JSON data in response to the request.

**4. CORS (Cross-Origin Resource Sharing):**  The instructions emphasize the need to enable CORS to allow GET requests from any origin. This is crucial for allowing the testing mechanism to communicate with the student's API.

**5. Testing Mechanism:** The system tests the API by sending a GET request with a query parameter `q` containing the task description.  The query parameter is URL-encoded:

```
curl -X 'GET' \
'http://127.0.0.1:8000/execute?q=What%20is%20the%20status%20of%20ticket%2083742%3F' \
-H 'accept: application/json'
```

This `curl` command simulates a GET request to the API, asking "What is the status of ticket 83742?".  The `-H 'accept: application/json'` header specifies that the client expects a JSON response.

**6.  Debugging Steps:** The student needs to fix their API implementation to:

*   Correctly handle the request and return a valid JSON response.
*   Address the `SyntaxError` and ensure the response conforms to JSON standards.
*   Ensure CORS is properly enabled to prevent cross-origin request errors.


In summary, the screenshot captures a common problem in API development: the API is not responding with correctly formatted JSON, preventing the testing mechanism from evaluating its correctness. The student needs to debug their API implementation to fix the JSON response and enable CORS.*



  
I am trying this for so long how to fix this plss guide me. thanking you

---

### Post #108 by **Biray Sursingh Purty** (ds-students)
*February 05, 2025, 14:14 UTC*
there is a problem in question 7 and 8, fast api question, when i click on save, both api calls happens at once at [http://127.0.0.1:8000](http://127.0.0.1:8000/), and i can run fast api app for question 7 or 8 for one only, suppose i check for question 7 it shows correct, also for question 8 i check it shows correct , but when i try to save one of the answer gets incorrected because of simultaneous calls by question 7 and 8 at this address [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

### Post #109 by **Khushi Dhankhar** (ds-students)
*February 05, 2025, 14:18 UTC*


> **Image Content:** *This screenshot shows a student completing a quiz or assignment in a data science course.  The question focuses on building an API to perform semantic search using text embeddings.

**Key Information:**

* **Task:** The student is asked to provide the API endpoint URL for a semantic search service.
* **Functionality:** The API receives a POST request with a JSON body containing:
    * `docs`: An array of document texts.
    * `query`: A search query string.
* **Process:** The API uses the `text-embedding-3-small` model to generate embeddings for the documents and query.  It then calculates cosine similarity to find the top 3 most similar documents.
* **Response:** The API returns a JSON response with a `matches` field, containing the contents (or identifiers) of the three most similar documents, ordered by similarity score (highest first).
* **Example Response (JSON):**
```json
{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}
```
* **CORS:** The student is instructed to enable CORS (Cross-Origin Resource Sharing) to allow `OPTIONS` and `POST` requests, potentially from any origin.
* **Correct Answer:** The student correctly identified the API endpoint URL as `http://127.0.0.1:8000/similarity`.  The system confirms this as correct.
* **Next Step:** The system will test the provided URL by sending a POST request with a randomly generated JSON body.
* **Timer:** A timer shows 04:15:56 remaining.
* **Score:** The student's current score is 8.5 out of 9.5.


The screenshot effectively assesses the student's understanding of API design, semantic search using embeddings, and handling CORS.  The use of a random JSON body in the final test suggests a robust check of the API's functionality beyond the provided example.*



while saving the 7th,8th question its alteranately getting incorrect

im getting 8.5 marks but while saving it gets deducted to 7 because of these 2 questions  
this is really very frustrating since im working on this for so long like 5-8hours but still facing the same issue  
what to do  
[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) [@s.anand](https://discourse.onlinedegree.iitm.ac.in/u/s.anand)

**Reactions:** ❤️ 1

---

### Post #110 by **Khushi Dhankhar** (ds-students)
*February 05, 2025, 14:39 UTC*


> **Image Content:** *This screenshot shows a student working on a coding assignment within a data science course.  The assignment involves using a large language model (LLM) API, specifically `gpt-40-mini`, to analyze sentiment.

**Key Information:**

* **Objective:** The goal is to build an API call that correctly analyzes the sentiment of a given text string, classifying it as GOOD, BAD, or NEUTRAL.  The assessment validates both API integration and proper message formatting.

* **API Interaction:** The student uses a dummy `httpx` library to simulate the API interaction. They are restricted to using only four functions: `httpx.get`, `httpx.post`, `response.raise_for_status`, and `response.json`.

* **Input Data:** The code snippet shows a JSON payload (`DATA`) designed for the API request.  It defines the model ("gpt-40-mini") and includes two messages: a system message instructing the LLM on the task and a user message containing the text to be analyzed.

* **Error:** The student's code is producing an error: "Error: The user message must be N PIxDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZk, not N PIxDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZK," This indicates a case sensitivity issue in the user message.

* **Code Snippet:** The student's JSON payload:

```json
DATA = {
"model": "gpt-4o-mini",
"messages": [
    {"role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL."},
    {"role": "user", "content": "N PIXDC6t EXfymclF e K x1XTpIULdX t6H LTa YGZk,"}
]
}
```

* **Grading:** The assignment has a score of 8.5/9.5, indicating near completion. A portion of the grade (0.75 marks) is dedicated to LLM token cost.

**Expert Analysis:**

The student's code is almost correct, but the error message clearly points to a capitalization problem within the "user" message.  The LLM is case-sensitive, and a single capital 'Z' instead of a lowercase 'z' causes the failure. Correcting this typo should resolve the issue.  The use of a dummy `httpx` library is a common pedagogical approach in teaching API integration to avoid unnecessary complexities or API key management during the learning process.*



  
in the 1st as well both the outouts are exactly same but its still showing error  
[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)

---

### Post #111 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 05, 2025, 14:56 UTC*
You can run 2 different severs on different port numbers.  
<http://127.0.0.1:8000> and <http://127.0.0.1:8001>

**Reactions:** 👍 1 ❤️ 1

---

### Post #112 by **Sudhish Narayan S** (ds-students)
*February 05, 2025, 15:26 UTC*
I tried checking the JSON Output in the Networks tab. I am getting error as “Method Not Found”. But, I have allowed POST Method for question 7 as POST method is used in the question. I also tried checking my API by sending a POST request by the same parameters as given by the Website. I am getting the proper response when I give an API request. Can you please help me out here? I have attached the screenshot of the error as Picture -1 and the correct output what I get as Picture-2. Please help me out as I am facing issue for all the API Questions though I am getting the right output. Thank You.  


> **Image Content:** *The screenshot shows a JSON response fragment indicating an error.  The key element `"detail"` has the value `"Method Not Allowed"`.

This is a standard HTTP error response (status code 405) indicating that the HTTP request method used (e.g., GET, POST, PUT, DELETE) is not supported for the requested resource.  The user likely attempted an operation on a server endpoint that doesn't allow that type of request.  For example, they might have tried to use a POST request on an endpoint designed only for GET requests.

To troubleshoot, the student needs to check the API documentation to see what HTTP methods are allowed for the specific endpoint they're targeting. They should also verify that they are using the correct method in their code.  The specific code causing the error is not shown in the image, only the error message itself.*

  


> **Image Content:** *The image is a screenshot showing a JSON-like structure, specifically a dictionary with a single key-value pair.  The key is "matches", and the value is a list of strings.  The strings appear to be excerpts from some sort of announcement or internal communication.

The key information is the content of the strings within the `matches` list. They likely describe a software product update and an expansion of a global IT support network. The detail is as follows:

* **Update 1:** The first string indicates a product update that addresses reported bugs and includes several enhancements.  No specific details about the bugs or enhancements are given.

* **Update 2:** The second string announces the approval of the expansion of a global IT support network.  Again,  no specific details regarding the expansion's nature or scope are provided.

* **Update 3 (Incomplete):** The third string is cut off, but appears to begin with "The internal...".  This suggests additional information exists that was not fully captured in the image.

The lack of detail in these updates suggests this might be a summary or notification rather than a complete report. The JSON-like formatting suggests the data may originate from a system designed to aggregate and present such updates.  The context of a data science course forum suggests this might be a snippet of data used in an example, perhaps related to natural language processing, text analysis, or data mining.*



---

### Post #113 by **Sudhish Narayan S** (ds-students)
*February 05, 2025, 16:00 UTC*
And for Question-9, I tried 80 prompts and I tried every different way, but I am not getting a Yess from the LLM. Can you please say how to proceed for that? Thank You

**Reactions:** 👍 1

---

### Post #114 by **Jayesh Bansal** (ds-students)
*February 05, 2025, 16:22 UTC*
import numpy as np  
def most\_similar(embeddings):  
words = list(embeddings.keys())  
dot\_product\_df =   
for i in words:  
for j in words:  
dot\_product\_df.append(np.dot(embeddings[i], embeddings[j]))  
return max(dot\_product\_df)  
print(most\_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

---

### Post #115 by **Jayesh Bansal** (ds-students)
*February 05, 2025, 16:23 UTC*
Jayeshbansal:

> print(most\_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))



> **Image Content:** *This screenshot shows a student's Python code within a data science course forum, along with a resulting `TypeError`. Let's break down the key aspects:


**1. The Python Code:**

The code snippet aims to find the word in a list (`words`) that has the highest cosine similarity to a reference word (implied by `embeddings[i]`). It calculates cosine similarity using the dot product of word embeddings.

```python
for j in words:
    dot_product_df.append(np.dot(embeddings[i], embeddings[j]))
return max(dot_product_df)
```

* **`for j in words:`**: This loop iterates through each word in the `words` list.
* **`dot_product_df.append(np.dot(embeddings[i], embeddings[j]))`**:  This line calculates the dot product between the embedding vector of the reference word (`embeddings[i]`) and the embedding vector of the current word (`embeddings[j]`). The result (a scalar value representing similarity) is appended to `dot_product_df`.  Crucially, `dot_product_df` is not defined in this snippet and needs to be initialized elsewhere in the code. `np.dot` implies the use of the NumPy library.
* **`return max(dot_product_df)`**: This line returns the maximum dot product value from the `dot_product_df` list, indicating the word with the highest similarity to the reference word.


**2. The Print Statement and its Output:**

```python
print(most_similar({"I experienced issues during checkout.": [...]}))
```

This line calls a function called `most_similar`. The function argument is a dictionary where the key is the sentence "I experienced issues during checkout." and the value is a NumPy array of numbers (likely word embeddings). The function's output is not shown in its entirety.


**3. The Error Message:**

```
TypeError: Z.runPython(...).toJs is not a function
```

This error indicates a problem outside the Python code itself. The error originates from a JavaScript function, `toJs`, being called on an object (`Z.runPython(...)`) that doesn't have this function defined. This suggests that the Python code is being executed within a JavaScript environment (likely a web-based Jupyter Notebook or similar platform), and there's a mismatch between how the Python output is handled in the JavaScript part of the system. The student is probably using a platform that mixes Python and JavaScript execution, and the bridge between the two is not working correctly.


**In Summary:**

The student's Python code is logically sound for computing cosine similarity, but the `TypeError` shows a crucial problem with the execution environment.  The student needs to investigate the JavaScript side of the platform to fix the `toJs` function issue.  They also need to initialize `dot_product_df` before the loop.  If `dot_product_df` is intended to be a pandas DataFrame, they should create one using `pd.DataFrame()` prior to using `.append()`.  Using `append()` repeatedly on a DataFrame in a loop is generally inefficient; list comprehension would be better, or `pd.concat()`.*



---

### Post #116 by **Jayesh Bansal** (ds-students)
*February 05, 2025, 16:32 UTC*


> **Image Content:** *This screenshot shows a student's interaction with a data science course forum.  The student is having trouble with an API endpoint.


**Key Information:**

* **Problem:** The student received a `TypeError: Failed to fetch` error when trying to access an API endpoint.

* **API Endpoint:** The expected format of the API URL is `http://127.0.0.1:8000/execute?q=`.  The `?q=` part indicates that a query parameter is expected, presumably containing the task or data to be sent to the API.

* **Instruction:** The forum message explains that a GET request will be sent to this URL with a query parameter `?q=...` containing the task. The response from the API will be verified against an expected response.  The order of arguments in the request must match the function definition (the server-side code).

* **Likely Cause of Error:** The `TypeError: Failed to fetch` suggests that the API call failed to retrieve any data.  The issue is likely with the provided `q` value in the API request, or the API server itself might be unavailable or misconfigured.  The student needs to investigate the `q` parameter's content and verify the API server's functionality.


**Code/Commands:**

The only code snippet is the URL:

`http://127.0.0.1:8000/execute?q=`

**Error Message:**

`TypeError: Failed to fetch`*



---

### Post #117 by **Arnav Raj ** (ds-students)
*February 05, 2025, 16:34 UTC*


> **Image Content:** *This screenshot shows a student working on a data science course assignment involving a similarity API.  Let's break down the key information:

**1. The Assignment:** The student is tasked with building or interacting with an API endpoint that takes a list of documents and a query string as input (using POST method), and returns the documents ranked by similarity to the query.  The example shows that "Contents of document 3" is considered the closest match to a given query, followed by "Contents of document 1", and then "Contents of document 2".

**2. The API Endpoint:** The API endpoint URL is `http://127.0.0.1:8000/similarity`.  The student has correctly identified this URL.

**3. CORS Issue and Solution:** The assignment instructions emphasize the importance of enabling Cross-Origin Resource Sharing (CORS) to allow OPTIONS and POST requests, possibly from any origin.  This is crucial for the API to be accessible from different domains (like the testing environment shown).

**4. Error and System Information:** The student initially received the error: `Error: Got incorrect matches: The project blueprint for migrating to a microservices architecture is complete., Our system maintenance schedule has been updated to minimize downtime., The IT support portal now features a self-service FAQ for common issues.` This indicates a problem with the student's implementation, but the error message is not directly related to the code.  The message suggests that system maintenance may have impacted the expected API behavior.

**5. Testing with POST Request:** The student is instructed to test the API by sending a POST request with a JSON body containing `docs` (a list of documents) and `query`. The screenshot shows a successful POST request using a tool like Postman or Thunder Client.

**6. POST Request Body and Response:** The POST request body used is:

```json
{
  "docs": ["Contents of document 1", "Contents of document 2", "Contents of document 3"],
  "query": "Your query string"
}
```

The corresponding successful response is:

```json
{
  "matches": [
    "Contents of document 1",
    "Contents of document 2",
    "Contents of document 3"
  ]
}
```

**7. Server-Side Code (Inferred):** The terminal output shows the server running using `uvicorn`:

```bash
$ python -m uvicorn q7_test:app --host 127.0.0.1 --port 8000 --reload
```

This suggests the student's backend is likely implemented using Python and the uvicorn ASGI server, presumably within a file named `q7_test.py`.  The `--reload` flag indicates the server automatically restarts upon code changes. The server logs confirm successful POST requests to `/similarity`.

**8. Overall Assessment:** The student's API call is successful (200 OK status) but the initial matches were incorrect.  The error message points to a potential system issue rather than a coding error. The student needs to investigate why the API is not returning the expected similarity scores and address the underlying issue.*



  
[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!

I m attaching my codes:

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["OPTION","POST"],  
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

        return {"matches": matched_docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}












```

---

### Post #118 by **Arulvadivelan V** (ds-students)
*February 05, 2025, 16:48 UTC*
Hi,

I’m sorry if I’m asking an unrelated question, But I’m very confused with the concept of generating the token from <https://platform.openai.com/api-keys>

Could any one suggest the step by step process? I couldn’t able to find that similar question asked by anyone since the conversations are vast.

Please guide me on this. Also do i need to use my personal mail id or iitm mail id for accessing this token

---

### Post #119 by **Arnav Raj ** (ds-students)
*February 05, 2025, 17:02 UTC*
yes you have to use your IITM email id . Use this link and login you will get your token:  
<https://aiproxy.sanand.workers.dev/>

**Reactions:** 👍 1

---

### Post #120 by **Jayesh Bansal** (ds-students)
*February 05, 2025, 17:51 UTC*


> **Image Content:** *This screenshot shows a question and answer thread from a data science course forum, likely related to API interaction and JSON handling.

**The Question:**  Asks for the correct API URL endpoint for a specific implementation.  It provides an example format: `http://127.0.0.1:8000/execute`.  The `127.0.0.1` indicates a localhost address.  The port number (`8000`) is significant as it specifies the port the application is listening on.  `/execute` is the endpoint path.

**The Attempted Answer:** The user provided `http://127.0.0.1:9000/execute` as their answer. This is very similar to the example, differing only by the port number. This suggests the user might be working on a similar but different setup or have encountered a port conflict.


**The Error Message:** The critical piece of information is the error: `SyntaxError: "[object Object]" is not valid JSON`. This indicates that the API response received from the given URL (`http://127.0.0.1:9000/execute`) is not properly formatted as JSON.  The API is returning `[object Object]`, which is a JavaScript representation of an object; this is not valid JSON.  The issue stems from how the server is responding to the request. The server-side code likely needs debugging to properly format its output as JSON.  This is crucial for client applications to interpret the data correctly.*



---

### Post #121 by **Aditya Kumar Sahu** (ds-students)
*February 05, 2025, 18:28 UTC*
The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to <http://aiproxy.sanand.workers.dev/openai/v1/embeddings> with required headers. And, then calculate `similarity_scores` simply using  
\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}  
which in python syntax is-

```
np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

```

---

### Post #122 by **Sudhish Narayan S** (ds-students)
*February 05, 2025, 18:33 UTC*
Sir, Regarding the embedding questions, I had posted earlier. Now, I am writing the error I faced. I tried to use the OpenAI API, but I am getting the error as “The Maximum Quota has reached”. I tried using 5 new API Keys from OpenAI, from 5 different accounts. So, I had to use SentenceTransformers, Alibaba gte model. So, as the model has changed, I think so it is expecting answer as got from OpenAI Model, but as I used Alibaba gte model, I am getting different result. Can you please explain how to solve this issue? This will be helpful in my future codes. I could do chat requests but it is not giving output for Embedding requests, I tried it multiple times with multiple different keys.Thank You  


> **Image Content:** *The screenshot shows an error message from a data science course forum.  The error is a quota exceedance.

The error message is formatted as a JSON-like object.  Specifically, the key `"error"` contains another key `"message"` with the following string as its value:

```
'You exceeded your current quota, please check your plan and billing details.'
```

This indicates that the user has surpassed their allotted resource limit (quota) within the platform. The user is advised to review their subscription plan and billing information to understand and resolve the issue.  The exact nature of the quota (compute time, data storage, API calls, etc.) is not specified.*



---

### Post #123 by **Sudhish Narayan S** (ds-students)
*February 05, 2025, 18:34 UTC*
This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You

```
from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))


```

---

### Post #124 by **Pururaj Singh Shekhawat** (ds-students)
*February 05, 2025, 18:43 UTC*


> **Image Content:** *This screenshot shows the interface of an online data science course platform.  Let's break down the key information:

* **Course Completion Status:** The top bar indicates the course ended on Wednesday, February 5th, 2025, at 11:59 PM IST.  The current score is 0.  There are "Check all" and "Save" buttons, suggesting a quiz or assignment.

* **User Information:** The user is logged in as `24f2005437@ds.study.iitm.ac.in`.  A "Logout" button is present. This strongly suggests the course is affiliated with the Indian Institute of Technology Madras (IITM).  The "ds.study" domain indicates a dedicated learning environment.


* **Discussion Forum:** A link is provided to join a discussion forum on Discourse. This points to an active community element of the course.

* **Recent Saves:** The "Recent saves" section indicates two instances where the user saved their progress:

    * `Loaded` from 5/2/2025, 11:20:33 pm. Score: 6
    * `Reload` from 5/2/2025, 11:20:20 pm. Score: 6

    The difference in timestamps is only 13 seconds suggesting possibly a quick save/reload of the assignment.  The score of 6 indicates previous progress on the assignment or quiz.

**In summary:** The screenshot shows the end screen of a data science course assignment or quiz on a platform likely hosted by IITM. The student, 24f2005437@ds.study.iitm.ac.in, has a previous score of 6 and now has a score of 0. There's an option to review and potentially resubmit the assignment.  The platform facilitates community interaction through a Discourse forum.*



  
i submitted the assignment on time but i am still getting assignment not submitted. And it also show zero marks. Same thing happened with graded assignment 2. [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

---

### Post #125 by **Shouvik Roy ** (ds-students)
*February 06, 2025, 03:04 UTC*
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)  
I have submitted ga3 still showing not submitted , why sir?  



> **Image Content:** *This screenshot shows a student's view of a graded assignment within a data science course, specifically focusing on Large Language Models.  Let's break down the key information:

**Course Information:**

* **Course Name:** TDS 2025 Jan GA3 - Large Language Models
* **Assignment:** Graded Assignment 3
* **Due Date:** 5 Feb 2025
* **Platform:**  An online assessment platform, likely custom-built for the course.  It features a "Check all," "Save," and "Reload" functionality.
* **Discourse Forum:**  The student is encouraged to use a Discourse forum for questions.

**Student Status:**

* **Login:** The student is logged in as `23f1001348@ds.study.iitm.ac.in`.
* **Current Score:** 0 (shown at the top of the page)
* **Recent Save:**  A previous save from 2/4/2025, 4:04:47 PM with a score of 9.5 points.
* **Submission Status:** The assignment is "Not Submitted."
* **Scores:**  Your Score, Peer Average, and Median Score are all displayed as "-" indicating the assignment has not been submitted for grading yet.


**Instructions:** The instructions explicitly state the following permissible actions:

* Students can check their answers multiple times.
* They can save their progress multiple times.
* Reloading the page is acceptable.
* Browser-based security restrictions can be disabled for troubleshooting purposes.
* Any resources, including the internet, ChatGPT, external libraries, and frameworks are permitted.
* "Hacking" the code to obtain answers is allowed.
* The student must run multiple servers concurrently during checking and saving actions.


**Overall:** The screenshot displays a relatively open and flexible online exam environment where students are encouraged to utilize any resources at their disposal.  The emphasis is on understanding the concepts and leveraging various tools for problem-solving.  The fact that "hacking" is permitted suggests a focus on learning and problem-solving over strict adherence to traditional exam rules.*



---

### Post #126 by **Shouvik Roy ** (ds-students)
*February 06, 2025, 03:08 UTC*
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)  
please reply why its showing not submitted in ga3 but i have submitted that  



> **Image Content:** *This screenshot shows a graded assignment from a data science course, specifically module 3 on Large Language Models, within the TDS 2025 Jan GA3 exam.

**Key Information:**

* **Exam Name:** TDS 2025 Jan GA3 - Large Language Models
* **Module:** Module 3: Large Language Models
* **Assignment:** Graded Assignment 3 (Due: 5 Feb 2025)
* **Submission Status:** Not Submitted
* **Current Score:** 0
* **Recent Save:** A previous save exists from 2/4/2025, 4:04:47 PM with a score of 9.5.  This can be reloaded.
* **Exam Instructions:**  The instructions emphasize the freedom to use any resources (internet, ChatGPT, etc.), the ability to check answers multiple times, and the requirement that multiple servers must be running simultaneously during the exam.  The system will accept multiple saves, and the last saved version will be graded. Browser issues are acknowledged, and students are advised to disable security restrictions if needed.  Importantly, "hacking" the code to find answers is explicitly permitted.
* **User Login:** The user is logged in as `23f1001348@ds.study.iitm.ac.in`.
* **Discourse Forum:** A link to a Discourse forum is provided for questions.


**No code, commands, or error messages are visible in the screenshot.***



---

### Post #127 by **Srividhya** (ds-students)
*January 30, 2025, 10:42 UTC*
[@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton), [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)  
Both the api based questions i am unable to get the output it always says bad request  



> **Image Content:** *This screenshot shows a Python script within a data science course, likely focused on natural language processing or query parsing.  The student is debugging a function called `parse_query` which attempts to interpret user queries.

**Key Information:**

* **`parse_query` function:** This function takes a query string as input and uses regular expressions (`re.match`) to identify different query types.  Currently, it handles two types:
    * **"Arrange meeting"**:  It extracts the date, time, and meeting room from queries like "Arrange meeting 2025-12-17, 06:09, room: Conf1".  The regular expression is quite complex, allowing for variations in the wording and formatting.
    * **"Show my expense balance"**: It aims to extract the employee ID from queries like "Show my expense balance for employee <employee_id>".  The regular expression is less robust than the one for meeting scheduling.

* **Regular Expressions:** The script uses `re.match` with complex regular expressions to parse the input queries.  These regular expressions are case-insensitive (`(?i)`) and capture different parts of the query using parentheses for group extraction.  The error messages strongly suggest the regular expressions aren't correctly handling edge cases or variations in the input query structure.


* **Error Messages:** The terminal output reveals several "400 Bad Request" and a "404 Not Found" error from HTTP requests. This indicates that the queries generated by `parse_query` are not being properly understood or processed by a backend service (perhaps a web API).  The "Query format did not match any predefined patterns" messages suggest the regular expression matching is failing, meaning the code isn't correctly identifying the query type before making the API call.

* **Debugging:** The `print` statements within the `if` blocks indicate the student is attempting to debug the function by printing the matched groups from the regular expressions. This helps track which parts of the query are being extracted successfully.

**Code Snippets:**

The key code snippets are the regular expressions and the function structure:

```python
def parse_query(query: str):
    # ... other code ...

    # Match "Arrange meeting 2025-12-17, 06:09, room: Conf1"
    match_schedule_meeting = re.match(
        r"(?i)(arrange\s*meeting|schedule\s*a\s*meeting)\s*(?:on\s*)?(\d{4}-\d{2}-\d{2})"
        r"\s*,\s*(\d{2}:\d{2})\s*,\s*room:\s*(.*)",
        query
    )

    # ... more code ...

    # Match "Show my expense balance for employee <employee_id>"
    match_expense_balance = re.match(r"(?i)show\s*my\s*expense\s*balance\s*for\s*employ",
        query
    )

    # ... rest of the function ...
```


**Expert Analysis Conclusion:**

The student is attempting to build a query parser using regular expressions, but the current implementation has flaws.  The regular expressions are likely too specific or not handling all the expected variations in user input.  The 400 Bad Request HTTP errors are the most important feedback: they mean that the parsed queries are not formatted correctly for whatever service they're being sent to.  The student needs to refine their regular expressions, possibly add more robust error handling, and thoroughly test their code with a wider variety of inputs to fix the issues and resolve the errors.  Debugging the regular expressions is the first step; a more thorough approach might involve using a more powerful parsing technique or a dedicated NLP library.*



  



> **Image Content:** *This screenshot shows a student working on a data science course exam.  The exam question involves calling a remote function via an API endpoint.

**Key Information:**

* **Exam:** The student is taking an exam on a platform named `exam.sanand.workers.dev`.  The specific section is `/tds-2025-01-ga3#hq-function-calling`.
* **Deadline:** The exam is due Sunday, February 2nd, 2025, at 11:59 PM IST.
* **Current Score:** The student currently has a score of 6.5 out of 9.5.
* **Function Definition:** The student is given a function definition in JSON format:

```json
{
  "name": "get_ticket_status",
  "arguments": "{\"ticket_id\": 83742}"
}
```

* **API Endpoint:** The student is asked to provide the API URL endpoint for their implementation.  The suggested format is `http://127.0.0.1:8000/execute`.  The student provided this URL.
* **Error:** The student received a `Error: Failed to fetch: Bad Request` error when attempting to access this endpoint. This suggests a problem with their API setup or the request itself.  The error likely indicates the server received a request but couldn't understand or process it.  The server likely expects the query parameter `?q=...` (containing the function call and arguments) to be included in the request.
* **CORS:** The instructions emphasize the importance of enabling CORS (Cross-Origin Resource Sharing) to allow GET requests from any origin. This is a common issue when making requests from a browser to a different domain or port.
* **Further Testing:** The system will send a GET request with a query parameter `?q=` containing a task, and will check that the response matches expectations.  The order of arguments in the GET request must match the function definition.
* **Additional Question:** A separate, smaller task requires getting an LLM to say "Yes".

**Issues and Next Steps:**

The main issue is the `Bad Request` error.  The student needs to investigate why their API is returning this error.  They should:

1. **Verify CORS:** Confirm that CORS is properly configured on their server to allow requests from the origin making the request.
2. **Check Request:** Ensure the GET request includes the `?q=` parameter correctly formatted with the task data, including the function name and arguments from the `function definition` in the correct order.
3. **Debug Server-Side:**  Inspect server logs to identify the reason for the `Bad Request`.  The problem could be in how the server parses the request, a missing endpoint, or other server-side logic.

The student needs to resolve the API issue to complete the exam successfully.*



  
all other questions i have finished. even in Ga2 all these api and flask creates a lot of issues. if there is any complete guide to understand this also pls help us.

---

### Post #128 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*January 30, 2025, 22:22 UTC*
Hi [@23ds1000022](https://discourse.onlinedegree.iitm.ac.in/u/23ds1000022) ,

Check network tab, there check for response of `http://127.0.0.1:8000/api` request.

**Reactions:** ❤️ 1

---

### Post #129 by **SAKSHI PATHAK** (ds-students)
*February 01, 2025, 12:44 UTC*
I have counted the number of tokens in gpt-4o-mini but when I was entering the answer in portal it was showing incorrect please take a look and provide a solution for it .  



> **Image Content:** *This screenshot shows the OpenAI Platform's text completion interface.  A user has entered a large number of seemingly random alphanumeric strings into the input box.  The platform has processed this input and provided the following information:

* **Model Selection:** The user has chosen either GPT-4 or GPT-4 mini.

* **Input Text:** The input box contains a long comma-separated list of seemingly random strings:

```
eWHNetl, eGEjb, 9, kZFurXr, Pnti2d0, HnV66V0, cR9zhYBi, NL, 9T1DU3, DaRw,
9irI10, 6AiKKkHU, FJ7XYuT, ZBfU30, TH, B, EuaXvr4VYp, YC, li6J4dJPn, pTWN,
EZshp, eET, U163LMWSW, D, s, VvBmRL3t, O3YTvv, mx6N, QLVNE, PF, Btl1SAW8jP,
F1jqXwyZy, uQJiS, XjNNS, 89NSMaNWrh, z017vbI, Hzb2, TZbpJdLQ, DRmAkXE,
bjq8QYisGG, VVJØDT, 2VL, dHyrz, kOFDUi3pf, joAB7U1c, Mzhkjz8oQI, J, L8wIWIF,
QAQ11c5vQ, mNNOQ4RJFX, xvX, rMeYNv, pC30jjkI, yguY0s85, fDlnOqd, iPWS5, xOkd,
tSWIafaO, 7Kiy7Imj, FWs1n2s, LGsZ18GED, g6Skq, I3nUSc2, Nh6b, SOQX, 8,
q0lrAnQIz, OcyWnSIE, N5Uk, C
```

* **Token and Character Count:**  The platform indicates that the input consists of 406 tokens and 625 characters.

**Analysis:**

The input data appears nonsensical.  It's highly unlikely that this represents a real-world data science problem. This may be a test case for the user exploring input limits or model behavior, perhaps related to tokenization, or a contrived example for a discussion within the forum. The lack of context from the surrounding forum discussion prevents a more definitive analysis.*



---

### Post #130 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 01, 2025, 16:06 UTC*
There are few more tokens for the user prompt, I think if you add 7 or 8 then you would get correct answer.

Other way to do this question is send a request to anand sir’s aiproxy and in response you will get number of input tokens.

**Reactions:** 👍 1 clap 1 ❤️ 1

---

### Post #131 by **Sakthivel S** (ds-students)
*February 01, 2025, 16:32 UTC*
I inspected the JavaScript code of this website, I saw that the answer took my input and added 7 to it, why is it programmed this way? Even if I were to use the AI proxy that was given shouldn’t the number of tokens remain unaffected?

---

### Post #132 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 01, 2025, 17:03 UTC*
When you send request to openai through anand sir’s proxy it takes some tokens for user prompt.

When you use tokenizer from openai’s webpage then it doesn’t take care of that.

**Reactions:** ❤️ 2

---

### Post #133 by **Dwarakesh** (ds-students)
*February 03, 2025, 18:11 UTC*
How to answer the 3rd question in ga 3 i have to no clue (tired inspecting its html pages)

---

### Post #134 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 03, 2025, 22:25 UTC*
[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

### [2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

**Reactions:** 👍 1 ❤️ 1

---

### Post #135 by **SAKSHI PATHAK** (ds-students)
*February 03, 2025, 19:44 UTC*
Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

Q7 & Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.

```
`from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only this specific origin
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Allow only POST and OPTIONS methods
    allow_headers=["Content-Type", "Authorization"],  # Allow only specific headers
)

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-003",  # Use the correct model
        input=text
    )
    return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    docs = request.docs
    query = request.query
    query_embedding = get_embedding(query)
    doc_embeddings = [get_embedding(doc) for doc in docs]
    
    # Cosine similarity
    similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
    ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
    
    return JSONResponse(content={"matches": ranked_docs[:3]})

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
    return {"message": "Welcome to the similarity API!"}
`

```

and for Q8

```
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

    if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)
    
    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
    
    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]
    
    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)
    
    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

```

Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this. [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) , [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) , [@Saransh\_Saini](https://discourse.onlinedegree.iitm.ac.in/u/saransh_saini)

---

### Post #136 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 03, 2025, 22:40 UTC*
Hi Sakshi

Sakshi6479:

> Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.



[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

### [2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.



---

For question 7

Sakshi6479:

> ```
> import openai
>
> ```

You won’t be able to send request through openai python module, here is one example how you would make a request

```
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)

```

You would need to use professor Anand’s proxy or some other api key through which request can be made.  
Url’s for free api keys:

1. [AI Proxy](https://aiproxy.sanand.workers.dev/)
2. [OpenAI GPT-4o · GitHub Models](https://github.com/marketplace/models/azure-openai/gpt-4o/playground)

The way to use api’s is demonstrated in live sessions, also refer to this documentation [sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy).

---

For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like `order` and `cancel_order`.

Kind regards

---

### Post #137 by **Shalini Saravanan** (ds-students)
*February 03, 2025, 09:24 UTC*
Hello sir,

While working on this question, I’m encountering this problem. It looks like the request is being made successfully (and I verified it by a POST request via Postman ), however while submitting my URL at the assignment portal, I’m getting an error.



> **Image Content:** *This screenshot shows log output from a data science course, likely related to a project involving a similarity search engine or a database query system. Let's break down the key information:

**1. HTTP Requests:**

The log displays two HTTP requests:

* `INFO: 127.0.0.1:59423 "OPTIONS /similarity HTTP/1.1" 200 OK`: This is a preliminary request (OPTIONS) to the `/similarity` endpoint, likely checking the server's capabilities before a more substantial request. The `200 OK` status code indicates success.

* `INFO: 127.0.0.1:59423 "POST /similarity HTTP/1.1" 200 OK`:  This is a `POST` request to the same endpoint, implying the sending of data (likely a search query) to the server. The `200 OK` status again signifies successful processing.  The `POST` request is likely the core action in the system.

**2. Database Interaction:**

The log reveals interactions with a database:

* `Collection reset successfully!`:  An existing collection (likely of documents) was cleared.
* `Created new collection: documents`: A new collection, named "documents," was created.
* `Added 10 new documents to the database.`: Ten new documents were added to the "documents" collection.  This implies a database such as MongoDB is being used.

**3. Search Query and Results:**

* `Searching for query: How is our internal training addressing cybersecurity challenges?`: This is the core query the student (or the code) submitted to the search engine or database.
* `Found matches: [...]`: The system returned three matching documents, the content of which provides information about employee cybersecurity training, handbook updates, and automated testing protocols.  This section highlights the successful functionality of the search functionality built into the system.

**4. Inference:**

The student is working on a project likely involving:

* **A database:**  Storing and managing documents.
* **A similarity search engine or API:** Used to search documents based on a given query.  The use of HTTP requests implies a web service architecture.
* **Text processing:** Extracting information and answering queries based on text content.

The overall success of the operation is confirmed by the `200 OK` responses to both HTTP requests, and the successful query answering. The project is likely demonstrating a practical application of information retrieval or natural language processing techniques.*



  



> **Image Content:** *This screenshot shows a question and answer thread from a data science course forum.

**The Question:**

"What is the API URL endpoint for your implementation? It might look like: `http://127.0.0.1:8000/similarity`"

**The Answer:**

The student provided the URL `http://127.0.0.1:8000/similarity`  as the API endpoint. However, there is a warning indicator (an exclamation mark inside a circle) next to the answer box, suggesting a problem.

**The Error Message:**

Below the answer, an error message is displayed:

`Error: Got incorrect matches: Employee training on cybersecurity best practices is being rolled out company-wide., The staff handbook has been updated to reflect current operational policies.,Our quality assurance team has implemented automated testing protocols.`

**Analysis:**

The error message indicates that the student's API endpoint returned unexpected text. Instead of relevant data, it returned three sentences related to company policies and training.  This suggests a problem with the student's implementation of the API or a misconfiguration of the API endpoint itself. The student likely needs to debug their code to fix the issue and provide the correct API response.  The `127.0.0.1` IP address is a common localhost address, indicating the API is running locally on the student's machine.*



I even tried deploying on a public URL using render. My guess is there is a formatting issue or it’s not sorting correctly based on the similarity score and not returning the top 3.

Would appreciate if I can get some clarity on the same

Thanks and Regards  
Shalini

---

### Post #138 by **SHAON BALLAV** (ds-students)
*February 03, 2025, 22:26 UTC*
Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.



> **Image Content:** *This screenshot shows a Postman request to a FastAPI similarity endpoint at `http://127.0.0.1:8000/similarity`.  The request is a POST request with a JSON body containing a list of strings.  Let's break down the key elements:

**1. Request Details:**

* **URL:** `http://127.0.0.1:8000/similarity`  This indicates a local development server (127.0.0.1) on port 8000. The `/similarity` path suggests an endpoint designed for comparing text similarity.
* **Method:** `POST`. This implies the request sends data to the server for processing, rather than retrieving data.
* **Authorization:** `No Auth`.  The request doesn't require any authentication or authorization tokens.
* **Body (JSON):**
```json
{
  "matches": [
    "FastAPI is great for APIs.",
    "Embedding models improve NLP.",
    "Machine learning is evolving."
  ]
}
```
This JSON payload sends three sentences to the server for similarity analysis.  The `matches` key suggests the server will likely return similarity scores or comparisons between these input sentences.

**2. Response:**

* **Status Code:** `200 OK`. This indicates a successful request. The server processed the request correctly.
* **Response Time:** `17.26 s`.  The server took 17.26 seconds to respond. This is quite slow; it might indicate an issue with the server or the request itself (though potentially normal for a development environment).
* **Response Size:** `232 B`. The response is small, suggesting a concise answer, potentially just similarity scores or a short JSON indicating success.

**3. Overall Assessment:**

The screenshot shows a successful test of a FastAPI endpoint built for semantic similarity analysis.  The relatively slow response time might warrant further investigation. The absence of any error messages or warnings suggests the server is responding as expected. This is likely a snippet from a data science course demonstrating a text similarity API and its usage.*



I had used (well gpt) the below two decorators to format:

```
class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)


.........

return SearchResponse(matches=sorted_matches[:3])

```

It basically checks the Request and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that

---

### Post #139 by **Jivraj Singh Shekhawat** (Course TA, ds-students)
*February 03, 2025, 22:45 UTC*
```
{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}

```

Check if your response is in this format.

kind regards  
Jivraj

**Reactions:** ❤️ 1

---

### Post #140 by **Matlin Jeleshiya ** (ds-students)
*February 05, 2025, 18:48 UTC*
Does the final submission get graded, or is the highest-scoring submission considered?

I’m facing an issue where my score dropped from 8 to 6.5 when I checked all the answers one last time before submitting. I suspect the drop is due to the 3rd and 7th questions.



> **Image Content:** *This screenshot shows a list of "Recent saves" from a data science course platform.  The platform appears to allow users to save their work and provides a timestamp and a score for each save.  Each entry displays a "Reload" button, suggesting the user can restore their work to a previous state using this button.

The three most recent saves were made on February 5th, 2025 at the following times and scores:


* **11:59:18 PM:** Score: 6.5
* **11:30:37 PM:** Score: 8
* **10:44:08 PM:** Score: 6.5

The scoring system is unknown, but likely reflects progress or accuracy in a task or assignment within the course.  The high score of 8 compared to the other 6.5 scores suggests this may be a graded element.  The fact that the user is saving frequently indicates they are actively working on the assigned material. There is no code, commands, or error messages present in the image.*



---

### Post #141 by **Carlton D'Silva** (Regular, ds-students)
*February 06, 2025, 06:05 UTC*


> **Image Content:** *This screenshot shows the instructions for a data science course exam, specifically "TDS 2025 Jan GA3 - Large Language M".  Key information includes:

* **Exam Details:** The exam ended on Wednesday, February 5th, 2025, at 11:59 PM IST.  The student's current score is 0.

* **Instructions:** The instructions are quite permissive, encouraging students to utilize any resources available.

* **Assessment Mechanics:**  The system allows for multiple checks and saves.  Only the last saved submission will be graded. The questions remain consistent except for randomized parameters. Browser issues are anticipated, suggesting troubleshooting steps like disabling security restrictions or using a different browser.  The exam explicitly permits "hacking" the code to find answers.

* **Technical Note:** The exam runs on multiple simultaneous servers; all must be active during checking and saving to ensure proper functionality.

* **No Code:** There is no code visible in the provided screenshot.  The instructions focus on the exam's rules and available resources.*



The score drops because some questions may require you to either keep a server turned on or some dynamic changes may occur for some questions (The dynamic changes are intentional in some questions, in order to get students to learn by doing. So if you solved everything and the score is the maximum… just make that your last submission. The score you see is the score you will get for your last submission).

If you want check a question without submitting. Then just use the check button instead. But your last submission is whats scored.

---

### Post #142 by **Pururaj Singh Shekhawat** (ds-students)
*February 06, 2025, 07:21 UTC*
Same problem with my submission

---

### Post #143 by **Carlton D'Silva** (Regular, ds-students)
*February 06, 2025, 14:43 UTC*


> **Image Content:** *This screenshot shows a bar chart visualizing the distribution of active scores for students in a course labeled "GA3".  The chart's title is "GA3 Active Score Distribution".

The x-axis represents score ranges (0-10, 10-20, 20-30, etc., up to 90-100), and the y-axis represents the number of students achieving scores within those ranges ("GA2 Student Count").

Key observations:

* **Skewed Distribution:** The distribution is heavily skewed to the right, indicating a large number of students achieved high scores (90-100).
* **High-Scoring Students:**  A substantial portion of students (249, as indicated in the legend) scored between 90 and 100.
* **Lower Scores:** A smaller number of students obtained scores in the lower ranges (0-10, 10-20, etc.).  The lowest range (0-10) shows only 12 students.
* **No Outliers:** There are no significant outliers visually apparent in the data.

The chart provides a clear summary of student performance in GA3, highlighting a strong overall performance but with a notable number of students in the lower score brackets.  The legend clearly shows the relationship between the bar height and the student count.  The chart is well-labeled and easy to interpret.*



For those that are interested.

---

### Post #144 by **Ayush Kumar Shaw ** (ds-students)
*February 08, 2025, 01:44 UTC*
sir why the GA marks is not being reflected in the course page. We are getting a sign of non submission.  
Is there any way getting the score.

---

### Post #147 by **Shahil Khan** (ds-students)
*February 09, 2025, 15:16 UTC*
Hello sir ,I find a issue with submission of GA4. Actually i submitted ga3 on “[Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga3)” with full marks but in the course >grade portal it is saying it is not submitted. what’s the issue is this?

---

### Post #148 by **Imran Ashraf** (ds-students)
*February 10, 2025, 20:31 UTC*
I also have same problem

---

### Post #149 by **Andrew David** (ds-students)
*February 11, 2025, 18:55 UTC*
can you please reply?  
[@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj) [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton)

---

### Post #152 by **SHAIK YASIR HAMEED** (ds-students)
*May 24, 2025, 17:22 UTC*
Error: Invalid promptfooconfig.yaml: Missing required assertion for: <https://api.github.com/orgs/>  
for 14th Question

```
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - file://prompt.json

providers:
  - openai:gpt-4o-mini
  - openai:gpt-4o-mini
  - openrouter:openai/gpt-4o-mini
  - openrouter:openai/gpt-4.1-nano
  - openrouter:google/gemini-2.0-flash-lite-001
  - openai:gpt-4o-mini

defaultTest:
  vars:
    system_message: file://system_message.txt
    previous_messages:
      - user: Who founded Facebook?
      - assistant: Mark Zuckerberg
      - user: What's his favorite food?
      - assistant: Pizza

tests:
  - vars:
      question: Did he create any other companies?
  - vars:
      question: What is his role at Internet.org?
  - vars:
      question: Will he let me borrow $5?
  - vars:
      question: Did he create any other houses?
  - vars:
      question: Did he create any other hospitals?
  - vars:
      question: "Tell me about the OpenAI GitHub org"
    assertions:
      - responseStatus: 200
      - responseJsonContains:
          key: login
          value: "openai"
      - responseJsonHasKey: public_repos
  - vars:
      question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
    assertions:
      - contains-all:
          values:
            - "https://api.github.com/orgs/apple/repos"
            - "per_page=2"
            - "sort=stars"
            - "direction=desc"
            - "Authorization: Bearer"
      - llm-rubric:
          instruction: |
            Evaluate the response for:
            - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
            - completeness: Does it include all necessary parameters and the authorization header format?
          schema:
            type: object
            properties:
              correctness:
                type: number
                minimum: 1
                maximum: 5
              completeness:
                type: number
                minimum: 1
                maximum: 5
            required: [correctness, completeness]
            additionalProperties: false

  # ✅ Required assertion related to https://api.github.com/orgs/
  - vars:
      question: "What does https://api.github.com/orgs/ return?"
    assertions:
      - contains: "https://api.github.com/orgs/"


```

**Reactions:** ❤️ 1

---

### Post #155 by **Tanmay** (ds-students)
*May 28, 2025, 12:10 UTC*
Question 4:  
I am trying this :

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image."},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
        }
      ]
    }
  ]
}

```

I am getting this error :  
Error: The image\_url.url must be the base64 data URL of the image  
I verified that my Base64 encoding for the image is correct ..

---

### Post #156 by **Ajit** (ds-students)
*May 29, 2025, 08:28 UTC*
Getting the same issue -

```
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 18 most-starred repositories
    from the "stripe" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/stripe/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=18'
        name: "Limits to 18 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "stripe"
          - Limits results to exactly 18 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder
        name: "LLM rubric: task compliance" ```
```

---

### Post #158 by **Puneet Bajaj** (ds-students)
*May 29, 2025, 15:59 UTC*
Try this - right click on image and click open in new tab, in the new tab you will see the base64 url of image in chrome tab url bar  
Hope this helps

---

### Post #159 by **Shiva varshney ** (ds-students)
*May 30, 2025, 08:32 UTC*
**Realizing the Value of Collaboration**

As I’ve been going through this course, one thing that’s really started to make sense to me is how important collaboration is. None of us can know everything — and that’s okay. We all have different strengths, and when we work together, especially on projects, those strengths really start to shine.

I’ve come to believe that collaboration isn’t just about dividing tasks, it’s about learning from each other, supporting one another, and finding smarter ways to solve problems as a team. It helps us get things done more effectively and on time, and honestly, it makes the whole learning process a lot more enjoyable.

This course is definitely helping me build that mindset, and I’m excited to keep growing through shared learning.  
if somebody feels the same then Reply , Thankyou

**Reactions:** ❤️ 1

---

### Post #160 by **Abhishek Sharma** (ds-students)
*June 01, 2025, 04:45 UTC*
For Question 3, I was able to enable the answer box but the answer is always saying that either it is not valid json format or Error: Model must be gpt-4o-mini, not undefined.

I have tried multiple approaches but the same issue even after using help from Chat GPT. Could any one tell what is the correct answer?? Thanks!

Here is my response for not valid json format error:

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": "json",
  "tool_choice": "auto",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "generate_addresses",
        "parameters": {
          "$schema": "http://json-schema.org/draft-07/schema#",
          "type": "object",
          "properties": {
            "addresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "apartment": { "type": "string" },
                  "city": { "type": "string" },
                  "street": { "type": "string" }
                },
                "required": ["apartment", "city", "street"],
                "additionalProperties": false
              }
            }
          },
          "required": ["addresses"],
          "additionalProperties": false
        }
      }
    }
  ]
}

```

---

### Post #161 by **Ajit** (ds-students)
*June 01, 2025, 06:06 UTC*
That’s true, that’s how real world works, working in silos doesn’t apply outside controlled environment. Pretty good course for the same purpose

---

### Post #162 by **Rohit_varma_1128** (ds-students)
*June 01, 2025, 06:28 UTC*
For Questions 8 to 10 of GA3 how and where should we host the URL to receive and handle the responses effectively?

---

### Post #163 by **Rohit_varma_1128** (ds-students)
*June 01, 2025, 07:11 UTC*
For qn 8-10, the API is working as expected locally, but I’m now unsure about how to **deploy** it in a way that allows you to send a POST request to a public URL.

---

### Post #164 by **Vishal Baraiya** (ds-students)
*June 01, 2025, 13:50 UTC*
```
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 16 most-starred repositories
    from the "linkedin" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting and limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/linkedin/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=16'
        name: "Limits to 16 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "linkedin"
          - Limits results to exactly 16 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder in the header
        name: "LLM rubric: task compliance"

```

## Error: Error: Invalid promptfooconfig.yaml: Your config must include at least 5 test assertions. [@carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton) [@s.anand](https://discourse.onlinedegree.iitm.ac.in/u/s.anand) [@Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/jivraj)

---

### Post #165 by **Rohit_varma_1128** (ds-students)
*June 01, 2025, 17:25 UTC*
Is jina AI still active ?

---

### Post #166 by **Parsh** (ds-students)
*June 01, 2025, 18:35 UTC*


> **Image Content:** *This screenshot shows instructions for a data science course assignment involving building a Retrieval Augmented Generation (RAG) system.  The goal is to create an API endpoint that answers questions from the TypeScript Book by returning relevant excerpts.

**Key Information:**

* **Task:** Build a RAG API that answers questions based on the TypeScript Book documentation ([https://github.com/basarat/typescript-book/](https://github.com/basarat/typescript-book/)).
* **API Endpoint:** The API should accept GET requests with a query parameter ` /search?q=question_text`.
* **Response Format:** The API should return a JSON object with at least the following fields:
    * `"answer"`:  The relevant excerpt from the documentation.
    * `"sources"`: (Optional) References to the source document(s).
* **Accuracy:** The response's `"answer"` field must contain the exact answer to the question.
* **CORS:** The API must enable CORS to allow requests from any origin.
* **Testing:** The system will test the endpoint by sending questions and checking for the expected answers in the response.
* **Example Questions and Answers:** Two example question-answer pairs are provided to illustrate the expected behavior.  These are:
    * Q: "What does the author affectionately call the => syntax?"
    * A: `fat arrow`
    * Q: "Which operator converts any value into an explicit boolean?"
    * A: `!!`
* **Endpoint URL:**  The student needs to provide the URL of their running API endpoint.  An example `http://localhost:8000/search` is given, and a test URL `http://127.0.0.1:8010/search` is shown.

**Code Snippets:**

The only code snippet present is the expected JSON response structure:

```json
{
"answer": "string containing the relevant documentation excerpt",
"sources": "optional: references to source document"
}
```

and the query parameter format:

`/search?q=question_text`

There are no error messages in the screenshot.*



  
Can someone tell me what was the output format of this question because i solved it and got the output which seemed correct enough to me but still got marked incorrect. Any help will be appreciated

---

### Post #167 by **HRITIK ROSHAN MAURYA** (Course TA, ds-students)
*June 02, 2025, 08:00 UTC*
One issue is there in

```
"response_format": "json"  // incorrect 

```

Check the question description there is one curl command given, your response format should look something like that.

---
