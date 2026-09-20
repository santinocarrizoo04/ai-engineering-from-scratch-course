import Groq from "groq-sdk";

const groq = new Groq({apiKey: process.env.GROQ_API_KEY});
const MODEL = process.env.LLM_MODEL || "openai/gpt-oss-120b";

async function main() {
    const response = await groq.chat.completions.create({
        model: MODEL,
        max_tokens: 256,
        messages: [
            {
                role: "system",
                content: "What is a neural network in one sentence?",
            },
        ],
    });

    console.log(response.choices[0]?.message?.content);
}

main();