# Android and Fire Tablet support

## Recommended deployment targets

- Android APK distribution
- Amazon Fire Tablet compatibility
- Touch-first UI and audio-first interactions
- Lightweight assets and low-latency prompts

## Notes

- Keep the game client responsive on lower-end devices.
- Avoid large model calls on every frame.
- Cache character dialogue and quest prompts locally when possible.
- Use the platform adapter to adjust runtime behavior for mobile devices.
