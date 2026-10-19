import asyncio, edge_tts, os
L=[l.strip() for l in open('voz/lines.txt',encoding='utf-8') if l.strip()]
V={'alex':('es-PE-AlexNeural','+4%','+12Hz'),'jorge':('es-MX-JorgeNeural','+4%','+10Hz'),'camila':('es-PE-CamilaNeural','+4%','+0Hz')}
async def main():
  os.makedirs('voz/out',exist_ok=True)
  for k,(v,r,p) in V.items():
    for i,t in enumerate(L):
      await edge_tts.Communicate(t,v,rate=r,pitch=p).save(f'voz/out/{k}_{i+1}.mp3')
asyncio.run(main())
