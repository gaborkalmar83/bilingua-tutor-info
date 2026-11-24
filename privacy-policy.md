# Privacy Policy - Bilingua Tutor

_Last updated: 2026-11-24. Covers Bilingua Tutor for Android (package `com.bilingua.tutor`), version 1.7._

Bilingua Tutor is published by **Kalmarium**, the controller for the purposes of data protection law. Contact: kalmariumservices@gmail.com

## The short version

- There is no Bilingua Tutor account and no server run by the developer. The developer does not receive your words, sentences, chats, voice, texts, progress or API keys.
- By default the AI tutor runs on your phone. With the on-device model, what you write and say to the tutor is not sent to any AI service.
- Text or audio leaves your phone only when you choose a feature that needs an online service. Each one is listed below, with what it receives. In those cases the data goes straight from your phone to that service, using your own key where a key is needed.
- No advertising. No analytics or tracking added by the developer. One bundled Google library can send its own technical diagnostics to Google; see "Advertising, analytics and diagnostics".
- The full version is a one-off purchase through Google Play. Google handles the payment.

## Data stored on your device

All of this stays in the app's private storage unless you export it, or Android backs it up for you (see "Android backup"):

- your settings, including the languages you chose, your level and the AI provider you selected;
- saved words and sentences, flashcards and their review schedule, the mistakes the tutor corrected, progress per grammar rule, daily activity and streaks;
- your chat history with Lucy, including the written transcripts of voice conversations;
- texts and articles you opened in the Reader;
- cached word meanings and cached translations of the grammar map;
- a usage record per AI model (number of calls, token counts, response times, errors), counted on the device only;
- API keys you enter. They are encrypted with AES-256-GCM using a key held in the Android Keystore, kept in a separate file that is excluded from Android backup, and sent only to the provider they belong to;
- the on-device AI model files you downloaded (about 2.6 GB for the default model), in the app's own folder on shared storage, removed when the app is uninstalled;
- audio clips of words and sentences made for AnkiDroid cards, and, if you use a cloud voice for "all voice in the app", the spoken clips fetched from that provider, kept in the app's cache so each line is fetched once. These clips contain the tutor's or dictionary voice, not yours;
- the trial start date and a "purchased" flag (see "Purchase and trial");
- a diagnostic log. It is off by default. One exception: if the app was closed abnormally (a crash, a freeze, or the system ending it for memory), Android's own record of that event is written to the log at the next start, whether or not the switch is on. The log holds technical details such as model names, timings and error traces, not the text you wrote. It stays on the device unless you choose to send or share it.

The app does not store recordings of your voice.

If the app crashes, the error is shown on screen for you to copy, and saved in a file on the device. It is sent nowhere unless you tap "Send report", which opens your own email app with the report filled in; you see what it contains and send it yourself. A problem report sent from Settings also contains the app version, Android version, phone make and model, and the name of the AI model in use.

**Android backup.** If Android backup is switched on for your device, Android can include the app's database (words, cards, progress, chat history, Reader texts), your settings, the diagnostic log and the saved crash file in your own Google backup, and copy them to a new phone. API keys, the purchase and trial record, and the AI model are excluded. That backup is run by Android and Google under your Google account, not by the developer.

**Your own backup file.** Settings - Backup & data can export your data to a file in a place you choose. API keys are left out unless you pick "Export with API keys", which the app warns about. Where that file goes is up to you.

## The AI tutor: on your device or with a provider you choose

**On your device (default).** Google's Gemma 4 model, or another on-device model you select, runs on the phone. Lucy's conversations, Sentence Lab analyses, Reader translations, word meanings, drills and voice-mode replies are then computed on the device, and your text is not sent to any AI service.

Downloading a model fetches one file from Hugging Face (huggingface.co) through Android's download manager. Hugging Face receives a normal download request (your network address and basic device information), and none of your text. Hugging Face privacy policy: https://huggingface.co/privacy

**A cloud provider (only if you select one and enter your own key).** The text needed for each request is sent directly from your phone to that provider: the tutor's instructions (which include your chosen languages and level, and any custom instructions you wrote), your message or sentence, the recent turns of the conversation, or the article sentences to translate. Your API key is sent with it to authenticate you. The provider's own terms and privacy policy apply, including how long it keeps the data.

| Provider | Address contacted | Set up by you | Provider's privacy policy |
| --- | --- | --- | --- |
| OpenAI | api.openai.com | Your own API key | https://openai.com/policies/privacy-policy |
| Anthropic (Claude) | api.anthropic.com | Your own API key | https://www.anthropic.com/legal/privacy |
| Google Gemini | generativelanguage.googleapis.com | Your own API key | https://policies.google.com/privacy |
| OpenRouter | openrouter.ai | Your own API key. The app's name and a website address identifying the app are sent with each request | https://openrouter.ai/privacy |
| Azure AI Foundry (Microsoft) | The endpoint of your own Azure resource | Your own endpoint, deployment and key | https://privacy.microsoft.com/privacystatement |
| Local server (Ollama, LM Studio or compatible) | The address you enter | Your own server; optional key | Whoever runs that server |

When you tap "Load models", the app asks that provider for its model list, which sends your key. Choosing OpenRouter also loads OpenRouter's public model catalogue, without a key.

The model benchmark in Settings sends built-in sample sentences, not your own data, to the models you include.

## Voice

**Dictation and voice mode on the phone (default).** When you tap the microphone, the app asks for microphone permission and uses Android's speech recognition. On Android 13 and later it prefers on-device recognition. If that is not available for the language, your phone's default speech service (on most phones, Google's) may process the audio online under its own policy. In this mode the app itself does not record, store or send audio; it receives the recognised text.

**Read-aloud.** Text is spoken by the text-to-speech engine installed on your phone. If you pick a voice marked as needing the internet, that engine's provider receives the text.

**Realtime voice provider (optional, off by default).** In Settings - Voice you can connect voice mode to a realtime speech model with your own key: OpenAI Realtime (api.openai.com), an Azure AI Foundry realtime deployment, or Azure Voice Live (both on your own Azure resource). If you turn this on:

- while a voice conversation is open, the app captures your microphone audio and streams it live to that provider, together with the tutor's instructions; the provider sends back the tutor's voice and written transcripts of both sides;
- the provider transcribes your speech with a speech-to-text model on its side;
- the transcripts are saved in your Lucy chat history on the device; the audio is not saved by the app;
- how long the provider keeps audio or transcripts is governed by its own terms and your account settings with it.

The app asks for your confirmation before a realtime voice provider is first used, and the voice session ends when you leave the voice screen or the app goes to the background.

**Cloud voice for all speech (optional).** With a realtime voice provider set to "All voice in the app", every word or sentence you play aloud (including clips made for AnkiDroid) is sent as text to that provider to be spoken, and the returned audio clip is kept in the app's cache.

Microphone audio is never sent to the developer.

## Reading articles

When you ask the Reader to fetch a web page, the app requests that page directly from the website, which sees a normal page request from your network address. Text you paste or share into the app is not sent anywhere by that act alone.

If you configure a text-extraction service in Settings - Advanced (none is set by default), the address of the page you fetch is sent to that service, which fetches the page for you. Its own privacy policy applies.

Sentences from an article are sent to your AI provider only when you ask for a translation or analysis and a cloud provider is selected.

## AnkiDroid (optional)

If you choose AnkiDroid for flashcards, saved words, sentences, corrections and their audio clips are handed to the AnkiDroid app on the same phone, with the permission AnkiDroid asks you to grant. Nothing leaves the device through this feature. What AnkiDroid does with its data afterwards (for example its own sync) is governed by AnkiDroid and AnkiWeb.

## Notifications (optional)

If you switch on the daily reminder, the app asks for notification permission and schedules a local reminder on the device. No push service and no server is involved.

## Purchase and trial

The app has a 14-day free trial of the AI features and a one-off in-app purchase through Google Play Billing. Google processes the payment under its own privacy policy (https://policies.google.com/privacy). The app never sees your card or payment details. It receives the purchase record from Google Play on your device and checks its signature there; the app does not send it to the developer. Like every Play developer, Kalmarium can see order information (such as order number, country and price) in the Google Play Console.

The trial start date and the "purchased" flag are stored on the device only, in a file that is excluded from Android backup. To tie the purchased flag to your device, the app computes a hash from the device's app-specific Android ID and the app's signing certificate. The hash stays on the device.

## Advertising, analytics and diagnostics

Bilingua Tutor contains no advertising and does not use the advertising ID. The developer has added no analytics, tracking or crash-reporting service and receives no usage data.

One third-party library inside the app can send its own technical diagnostics to its maker:

- **Google Play Billing and Google Play services.** These are Google's own components. Google describes how it handles data from them in its privacy policy (https://policies.google.com/privacy), and they may send Google technical diagnostics such as device and app information, performance figures and error codes. They do not receive the text you write or the audio you speak from this app.

## AI transparency (EU AI Act)

Bilingua Tutor is a language-learning aid. Lucy is an AI system, not a person. Under the EU AI Act (Regulation (EU) 2024/1689) this is a limited-risk use with transparency duties. The app is not used for biometric identification or categorisation, emotion recognition, employment, credit, law enforcement, or any automated decision with a legal or similarly significant effect on a person, and it does no profiling of its users. The feedback and scores it gives are for your own practice; they are not a certificate, an exam result or an assessment for any school or employer.

Where AI is used:

- **Generated by a large language model**, on your device or by the provider you connected: Lucy's replies and corrections, Sentence Lab verdicts, Reader translations and colour-coded analyses, word meanings, drills, conversation topic suggestions, translations of the grammar map into other languages, and the benchmark results.
- **Synthetic speech**: the tutor's voice is produced by your phone's text-to-speech engine or, if you connected one, by a realtime voice model.
- **Not AI-generated**: the grammar map (hand-written rules and examples), your flashcard schedule (a fixed spaced-repetition formula) and your statistics.

How it is labelled in the app:

- Settings - About states that Lucy's replies, Sentence Lab verdicts, translations and drills are generated by AI and can be wrong.
- AI answers in Lucy, voice mode, the Sentence Lab, the Reader and the word sheet carry an "AI-generated, can contain mistakes" label, and first-run setup tells you that Lucy is an AI, not a person.
- Next to Lucy's replies, on Sentence Lab results and in the word sheet there is a "Report this answer" action, and one in Settings - About. It opens a drafted email in your own mail app containing the answer, the app version and the model name; you see it and send it yourself. Nothing is sent automatically.

AI output can be wrong, including grammar corrections. Check anything important with a teacher or a reference work.

This section is a good-faith transparency statement about how the app works, not legal advice.

## Legal basis

The developer does not receive or store your personal data from the app, so in most respects it does not process it. Where data protection law treats the developer as responsible for a flow the app makes possible, the basis is your own request for that feature (performance of the service you asked for) and, for the microphone and for each online provider, your choice to switch it on. If you write to the developer, the legitimate interest in answering you.

## International transfers

The services above are operated by companies in various countries, including the United States. When you choose to use one, your device sends the data directly to it, and that provider's terms and privacy policy apply, including for any transfer outside your country. With Azure you choose the region of your own resource. The developer does not transfer your data anywhere, because the developer does not receive it.

## Retention

Data on your device is kept until you delete it or uninstall the app. Cached voice clips sit in the app's cache, which Android may clear when storage runs low. The developer keeps nothing, apart from emails you choose to send, which are kept only as long as needed to answer you and deal with the problem reported. Retention at an online provider is set by that provider.

## Deleting your data

- **In the app:** Settings - Backup & data - "Delete all data" removes your words, cards, review schedule, progress, chat history, Reader texts, settings and stored API keys. "Delete stored keys" removes only the keys. Individual words and cards can be deleted where they are listed.
- **Not removed by "Delete all data"** in version 1.7: the downloaded AI model (delete it in Settings - AI provider), cached voice clips, the diagnostic log and saved crash file (clear them in Settings - Advanced - Diagnostics), and the trial and purchase record. Uninstalling the app removes all of them.
- **Everything:** uninstall the app, or clear its storage in Android settings.
- **Android backup:** manage or delete device backups in your Google account (Google One or Google Drive - Backups).
- **Online providers:** delete data and API keys through that provider's account pages.
- **Purchase records** are held by Google Play under your Google account.

## Your rights

Under the GDPR and similar laws you have rights of access, correction, deletion, restriction, portability and objection, and the right to withdraw consent. The developer holds no personal data about you from the app, so in practice you exercise these rights yourself: your data is on your device and in your own accounts, and you can export it (Settings - Backup & data, and the export options in Words) or delete it as described above. You can withdraw microphone or notification permission in Android settings at any time. For data held by a third-party service, contact that service. If you email the developer, that email is used only to answer you. You can also complain to your local data protection authority.

## Children

Bilingua Tutor is not directed at children and is not intended for anyone under 16. The developer does not knowingly collect data from anyone, of any age.

## Security

API keys are encrypted at rest with the Android Keystore. Connections to the hosted services named in this policy use HTTPS or secure WebSocket. Plain HTTP is possible only for a Local server you add yourself on your own network (an address such as localhost, 192.168.x.x, 10.x.x.x or a .local name); the app refuses plain HTTP to any other address. Data sent to such a server is not encrypted in transit.

## Website

This website (tutor.kalmarium.com) is hosted on GitHub Pages, which receives your network address when you open a page; see GitHub's privacy statement (https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement). The website counts page views with a cookie-free script that stores nothing on your device and sends only the page address, the referring website and the country (derived from your network address, which is not kept). It is switched off if your browser sends Do Not Track.

## Closed test sign-up

If you ask to join the closed test by email, the developer uses the address and details you send only to add you to the test and to write to you about it, and deletes them after the test ends. Google receives your Google account address to run the test, under Google's privacy policy.

## Earlier versions

This policy describes version 1.7. Versions up to and including 1.6 were test builds that were not published on Google Play. They differed in these ways:

- AI answers carried no "AI-generated" label outside Settings - About, and there was no "Report this answer" action;
- the in-app privacy summary did not mention the realtime voice provider, and no confirmation was asked before microphone audio was first sent to it;
- a voice session with a realtime provider could stay connected after the app was sent to the background;
- plain HTTP to a Local server was not available on current Android versions.

## Changes to this policy

If this policy changes, the update will be posted at the same address with a new "last updated" date.

## Contact

Kalmarium - kalmariumservices@gmail.com
