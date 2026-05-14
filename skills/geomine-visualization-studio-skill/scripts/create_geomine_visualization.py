#!/usr/bin/env python3
"""Generate a standalone GeoMine Three.js visualization studio project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def default_scene() -> dict[str, Any]:
    return {
        "title": "Athabasca Uranium Concept Model",
        "subtitle": "Conceptual basin-margin unconformity scene for GeoMine visualization",
        "status": "conceptual",
        "crs": "not authoritative",
        "verticalExaggeration": 1.35,
        "camera": {"position": [4.7, 3.1, 5.6], "target": [0, -0.3, 0]},
        "layers": [
            {
                "id": "cover",
                "name": "Athabasca sandstone cover",
                "color": "#d8a657",
                "depth": 0.35,
                "thickness": 0.46,
                "note": "Conceptual basin cover sequence.",
            },
            {
                "id": "unconformity",
                "name": "Unconformity surface",
                "color": "#f4e7bb",
                "depth": -0.05,
                "thickness": 0.08,
                "note": "Regional contact used as an interpretive horizon.",
            },
            {
                "id": "basement",
                "name": "Graphitic basement package",
                "color": "#475569",
                "depth": -0.62,
                "thickness": 0.72,
                "note": "Conceptual basement conductor and structural host.",
            },
        ],
        "structures": [
            {
                "id": "fault-corridor",
                "name": "Reactivated fault corridor",
                "color": "#ef4444",
                "points": [[-2.1, -1.18, -0.8], [-0.9, -0.45, -0.2], [0.35, -0.08, 0.18], [1.9, 0.42, 0.72]],
                "note": "Illustrative fluid pathway; geometry not authoritative.",
            },
            {
                "id": "fluid-pathway",
                "name": "Hydrothermal fluid path",
                "color": "#fb923c",
                "points": [[-1.8, -0.95, 0.65], [-0.55, -0.28, 0.18], [0.18, -0.1, 0.05], [1.3, 0.18, -0.45]],
                "note": "Conceptual flow path for animation.",
            },
        ],
        "oreBodies": [
            {
                "id": "uranium-lens",
                "name": "Uranium lens",
                "color": "#facc15",
                "position": [0.08, -0.18, 0.07],
                "scale": [0.78, 0.12, 0.32],
                "note": "Visual mineralization marker only; not a resource estimate.",
            }
        ],
        "drillholes": [
            {
                "id": "ddh-01",
                "name": "DDH-01 concept trace",
                "color": "#111827",
                "from": [-1.35, 1.2, -0.7],
                "to": [-0.05, -1.05, 0.08],
                "note": "Example drill trace for visual storytelling.",
            },
            {
                "id": "ddh-02",
                "name": "DDH-02 concept trace",
                "color": "#334155",
                "from": [1.35, 1.1, 0.75],
                "to": [0.18, -1.0, 0.05],
                "note": "Example offset drill trace.",
            },
        ],
        "gisPoints": [
            {
                "id": "cdogs",
                "name": "CDoGS geochemistry lane",
                "color": "#38bdf8",
                "position": [1.35, 0.18, -0.85],
                "note": "Planned public geochemical source lane.",
            },
            {
                "id": "occurrence",
                "name": "Mineral occurrence lane",
                "color": "#a78bfa",
                "position": [-1.55, 0.05, 0.85],
                "note": "Represents occurrence evidence to verify.",
            },
        ],
        "timeline": [
            {
                "id": "basement-architecture",
                "label": "Basement architecture",
                "description": "Pre-existing basement structures define possible fluid pathways.",
            },
            {
                "id": "cover-and-unconformity",
                "label": "Cover and unconformity",
                "description": "Basin cover and unconformity provide stratigraphic context.",
            },
            {
                "id": "fluid-flow",
                "label": "Fluid flow",
                "description": "Conceptual hydrothermal pathway is shown as an interpretive tube.",
            },
            {
                "id": "modern-sampling",
                "label": "Modern evidence",
                "description": "Public geochemistry and occurrence lanes are evidence-planning markers.",
            },
        ],
        "provenance": [
            {
                "label": "NRCan CDoGS",
                "url": "https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm",
                "retrievalStatus": "planned",
                "limitations": "No live survey retrieval in this demo.",
            },
            {
                "label": "Saskatchewan GeoAtlas",
                "url": "https://gisappl.saskatchewan.ca/Html5Ext/index.html?viewer=GeoAtlas",
                "retrievalStatus": "planned",
                "limitations": "No live GeoAtlas layer query in this demo.",
            },
        ],
    }


def load_scene(path: Path | None) -> dict[str, Any]:
    if path is None:
        return default_scene()
    return json.loads(path.read_text(encoding="utf-8"))


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def package_json() -> str:
    return """{
  "name": "geomine-visualization-studio",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite --host 127.0.0.1",
    "build": "tsc -b && vite build",
    "preview": "vite preview --host 127.0.0.1",
    "verify": "node scripts/verify.mjs"
  },
  "dependencies": {
    "@react-three/drei": "^10.7.7",
    "@react-three/fiber": "^9.4.0",
    "lucide-react": "^0.552.0",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "three": "^0.181.2"
  },
  "devDependencies": {
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.2",
    "@types/react-dom": "^19.2.2",
    "@vitejs/plugin-react": "^5.1.0",
    "playwright-core": "^1.59.1",
    "pngjs": "^7.0.0",
    "typescript": "~5.9.3",
    "vite": "^7.2.2"
  }
}"""


def app_tsx() -> str:
    return r'''import { Canvas, useFrame } from "@react-three/fiber";
import { ContactShadows, Float, Html, OrbitControls } from "@react-three/drei";
import { Layers, MapPinned, Play, RotateCcw, ShieldAlert, Sparkles } from "lucide-react";
import { useMemo, useRef, useState } from "react";
import { CatmullRomCurve3, TubeGeometry, Vector3, type Group } from "three";
import { sceneData, type SceneData } from "./scene-data";
import "./styles.css";

type Vector = [number, number, number];
type SelectableKind = "Layer" | "Structure" | "Ore" | "Drillhole" | "GIS";

type SelectedObject = {
  id: string;
  name: string;
  note: string;
  kind: SelectableKind;
};

function asVector(value: readonly number[] | undefined, fallback: Vector): Vector {
  if (!value || value.length < 3) {
    return fallback;
  }
  return [Number(value[0]), Number(value[1]), Number(value[2])];
}

function Tube({
  points,
  color,
  radius = 0.035,
  active,
  onClick,
}: {
  points: readonly (readonly number[])[];
  color: string;
  radius?: number;
  active: boolean;
  onClick: () => void;
}) {
  const geometry = useMemo(() => {
    const curve = new CatmullRomCurve3(points.map((point) => new Vector3(point[0], point[1], point[2])));
    return new TubeGeometry(curve, 96, active ? radius * 1.45 : radius, 14, false);
  }, [points, radius, active]);

  return (
    <mesh geometry={geometry} castShadow receiveShadow onClick={onClick}>
      <meshStandardMaterial
        color={color}
        roughness={0.48}
        metalness={0.05}
        emissive={active ? color : "#000000"}
        emissiveIntensity={active ? 0.32 : 0.04}
      />
    </mesh>
  );
}

function LayerBlock({
  layer,
  active,
  onClick,
}: {
  layer: SceneData["layers"][number];
  active: boolean;
  onClick: () => void;
}) {
  const y = layer.depth;
  return (
    <group position={[0, y, 0]}>
      <mesh castShadow receiveShadow onClick={onClick}>
        <boxGeometry args={[4.8, layer.thickness, 2.8]} />
        <meshStandardMaterial
          color={layer.color}
          transparent
          opacity={active ? 0.88 : 0.62}
          roughness={0.76}
          metalness={0.02}
          emissive={active ? layer.color : "#000000"}
          emissiveIntensity={active ? 0.12 : 0}
        />
      </mesh>
    </group>
  );
}

function OreBody({
  ore,
  active,
  onClick,
}: {
  ore: SceneData["oreBodies"][number];
  active: boolean;
  onClick: () => void;
}) {
  return (
    <Float speed={active ? 1.8 : 0.6} floatIntensity={active ? 0.08 : 0.02} rotationIntensity={0.04}>
      <mesh position={asVector(ore.position, [0, 0, 0])} scale={asVector(ore.scale, [1, 0.2, 0.5])} castShadow onClick={onClick}>
        <sphereGeometry args={[1, 48, 24]} />
        <meshStandardMaterial
          color={ore.color}
          transparent
          opacity={0.88}
          roughness={0.3}
          metalness={0.18}
          emissive={ore.color}
          emissiveIntensity={active ? 0.42 : 0.16}
        />
      </mesh>
    </Float>
  );
}

function GisPoint({
  point,
  active,
  onClick,
}: {
  point: SceneData["gisPoints"][number];
  active: boolean;
  onClick: () => void;
}) {
  return (
    <group position={asVector(point.position, [0, 0, 0])}>
      <mesh castShadow onClick={onClick}>
        <sphereGeometry args={[active ? 0.105 : 0.075, 24, 16]} />
        <meshStandardMaterial color={point.color} emissive={point.color} emissiveIntensity={active ? 0.5 : 0.18} />
      </mesh>
      {active ? (
        <Html center distanceFactor={9} className="scene-label">
          {point.name}
        </Html>
      ) : null}
    </group>
  );
}

function Scene({
  selectedId,
  setSelected,
  animate,
}: {
  selectedId: string;
  setSelected: (object: SelectedObject) => void;
  animate: boolean;
}) {
  const group = useRef<Group>(null);
  useFrame((_, delta) => {
    if (animate && group.current) {
      group.current.rotation.y += delta * 0.18;
    }
  });

  return (
    <group ref={group} scale={[1, sceneData.verticalExaggeration ?? 1, 1]}>
      {sceneData.layers.map((layer) => (
        <LayerBlock
          key={layer.id}
          layer={layer}
          active={selectedId === layer.id}
          onClick={() => setSelected({ id: layer.id, name: layer.name, note: layer.note, kind: "Layer" })}
        />
      ))}

      {sceneData.structures.map((structure) => (
        <Tube
          key={structure.id}
          points={structure.points}
          color={structure.color}
          radius={0.035}
          active={selectedId === structure.id}
          onClick={() => setSelected({ id: structure.id, name: structure.name, note: structure.note, kind: "Structure" })}
        />
      ))}

      {sceneData.oreBodies.map((ore) => (
        <OreBody
          key={ore.id}
          ore={ore}
          active={selectedId === ore.id}
          onClick={() => setSelected({ id: ore.id, name: ore.name, note: ore.note, kind: "Ore" })}
        />
      ))}

      {sceneData.drillholes.map((hole) => (
        <Tube
          key={hole.id}
          points={[hole.from, hole.to]}
          color={hole.color}
          radius={0.018}
          active={selectedId === hole.id}
          onClick={() => setSelected({ id: hole.id, name: hole.name, note: hole.note, kind: "Drillhole" })}
        />
      ))}

      {sceneData.gisPoints.map((point) => (
        <GisPoint
          key={point.id}
          point={point}
          active={selectedId === point.id}
          onClick={() => setSelected({ id: point.id, name: point.name, note: point.note, kind: "GIS" })}
        />
      ))}
    </group>
  );
}

function objectList(data: SceneData): SelectedObject[] {
  return [
    ...data.layers.map((item) => ({ id: item.id, name: item.name, note: item.note, kind: "Layer" as const })),
    ...data.structures.map((item) => ({ id: item.id, name: item.name, note: item.note, kind: "Structure" as const })),
    ...data.oreBodies.map((item) => ({ id: item.id, name: item.name, note: item.note, kind: "Ore" as const })),
    ...data.drillholes.map((item) => ({ id: item.id, name: item.name, note: item.note, kind: "Drillhole" as const })),
    ...data.gisPoints.map((item) => ({ id: item.id, name: item.name, note: item.note, kind: "GIS" as const })),
  ];
}

export default function App() {
  const objects = useMemo(() => objectList(sceneData), []);
  const [selected, setSelected] = useState<SelectedObject>(objects[0]);
  const [animate, setAnimate] = useState(true);
  const [timelineIndex, setTimelineIndex] = useState(0);
  const cameraPosition = asVector(sceneData.camera?.position, [4.5, 3.2, 5.5]);

  return (
    <div className="app-shell">
      <aside className="left-panel">
        <div className="brand">
          <span className="brand-mark">
            <Sparkles size={24} />
          </span>
          <div>
            <h1>GeoMine Visualization Studio</h1>
            <p>{sceneData.subtitle}</p>
          </div>
        </div>

        <section>
          <div className="section-title">
            <Layers size={18} />
            Evidence Objects
          </div>
          <div className="object-list">
            {objects.map((object) => (
              <button
                key={object.id}
                className={selected.id === object.id ? "is-active" : ""}
                type="button"
                onClick={() => setSelected(object)}
              >
                <span>{object.kind}</span>
                <strong>{object.name}</strong>
              </button>
            ))}
          </div>
        </section>
      </aside>

      <main className="stage">
        <div className="stage-header">
          <div>
            <h2>{sceneData.title}</h2>
            <p>Status: {sceneData.status} | CRS: {sceneData.crs}</p>
          </div>
          <div className="toolbar">
            <button type="button" onClick={() => setAnimate((value) => !value)}>
              <Play size={18} />
              {animate ? "Pause" : "Animate"}
            </button>
            <button type="button" onClick={() => setSelected(objects[0])}>
              <RotateCcw size={18} />
              Reset
            </button>
          </div>
        </div>

        <div className="canvas-panel">
          <Canvas camera={{ position: cameraPosition, fov: 45 }} shadows>
            <color attach="background" args={["#eef3ee"]} />
            <ambientLight intensity={0.72} />
            <directionalLight position={[4, 6, 4]} intensity={1.2} castShadow />
            <directionalLight position={[-4, 2, -3]} intensity={0.35} />
            <Scene selectedId={selected.id} setSelected={setSelected} animate={animate} />
            <ContactShadows position={[0, -1.35, 0]} opacity={0.22} blur={2.4} scale={8} />
            <OrbitControls target={asVector(sceneData.camera?.target, [0, -0.4, 0])} enableDamping makeDefault />
          </Canvas>
        </div>

        <div className="timeline">
          {sceneData.timeline.map((event, index) => (
            <button
              key={event.id}
              type="button"
              className={timelineIndex === index ? "is-active" : ""}
              onClick={() => setTimelineIndex(index)}
            >
              <span>{String(index + 1).padStart(2, "0")}</span>
              {event.label}
            </button>
          ))}
        </div>
      </main>

      <aside className="right-panel">
        <section className="detail-card">
          <div className="section-title">
            <MapPinned size={18} />
            Selected Evidence
          </div>
          <h3>{selected.name}</h3>
          <p className="kind">{selected.kind}</p>
          <p>{selected.note}</p>
        </section>

        <section className="detail-card">
          <div className="section-title">
            <ShieldAlert size={18} />
            Caveats
          </div>
          <p>
            This scene is a research visualization. Conceptual geometry is not authoritative, visual proximity is not economic evidence,
            and mineralized shapes are not resources or reserves.
          </p>
        </section>

        <section className="detail-card">
          <div className="section-title">Timeline</div>
          <h3>{sceneData.timeline[timelineIndex]?.label}</h3>
          <p>{sceneData.timeline[timelineIndex]?.description}</p>
        </section>

        <section className="detail-card provenance">
          <div className="section-title">Provenance</div>
          {sceneData.provenance.map((source) => (
            <a key={source.label} href={source.url} target="_blank" rel="noreferrer">
              <strong>{source.label}</strong>
              <span>{source.retrievalStatus}</span>
              <small>{source.limitations}</small>
            </a>
          ))}
        </section>
      </aside>
    </div>
  );
}'''


def styles_css() -> str:
    return r'''* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  color: #18231f;
  background: #e9eee9;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

button {
  font: inherit;
}

.app-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 300px minmax(0, 1fr) 320px;
  gap: 0;
}

.left-panel,
.right-panel {
  padding: 18px;
  background: #f7f7f1;
  border-right: 1px solid #d7ded3;
  overflow-y: auto;
}

.right-panel {
  border-right: 0;
  border-left: 1px solid #d7ded3;
}

.brand {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 24px;
}

.brand-mark {
  width: 46px;
  height: 46px;
  border-radius: 10px;
  display: grid;
  place-items: center;
  color: #f8fafc;
  background: #256d4d;
}

h1,
h2,
h3,
p {
  margin: 0;
}

h1 {
  font-size: 20px;
  line-height: 1.1;
}

.brand p,
.stage-header p,
.kind,
.detail-card p,
.provenance small {
  color: #647067;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  color: #3d5549;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
}

.object-list {
  display: grid;
  gap: 8px;
}

.object-list button,
.toolbar button,
.timeline button {
  border: 1px solid #cfd8cf;
  border-radius: 8px;
  background: #ffffff;
  color: #17251e;
  cursor: pointer;
}

.object-list button {
  display: grid;
  gap: 4px;
  padding: 11px 12px;
  text-align: left;
}

.object-list span {
  color: #6c756d;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
}

.object-list button.is-active {
  border-color: #256d4d;
  background: #e6f2ea;
}

.stage {
  display: grid;
  grid-template-rows: auto minmax(0, 1fr) auto;
  min-width: 0;
  min-height: 100vh;
  padding: 18px;
}

.stage-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}

.stage-header h2 {
  font-size: 28px;
  line-height: 1.1;
}

.toolbar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.toolbar button {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 38px;
  padding: 0 12px;
}

.canvas-panel {
  position: relative;
  min-height: 420px;
  border: 1px solid #cfd8cf;
  border-radius: 8px;
  overflow: hidden;
  background: #eef3ee;
}

.canvas-panel canvas {
  display: block;
}

.timeline {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 8px;
  margin-top: 14px;
}

.timeline button {
  min-height: 52px;
  padding: 8px 10px;
  text-align: left;
}

.timeline span {
  display: block;
  color: #647067;
  font-size: 12px;
  font-weight: 800;
}

.timeline button.is-active {
  border-color: #256d4d;
  background: #dff1e4;
}

.detail-card {
  padding: 14px;
  border: 1px solid #d6ded5;
  border-radius: 8px;
  background: #ffffff;
  margin-bottom: 12px;
}

.detail-card h3 {
  margin-bottom: 6px;
  font-size: 18px;
}

.kind {
  margin-bottom: 10px;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.provenance {
  display: grid;
  gap: 8px;
}

.provenance a {
  display: grid;
  gap: 3px;
  color: inherit;
  text-decoration: none;
  border-top: 1px solid #edf0ec;
  padding-top: 8px;
}

.provenance span {
  color: #256d4d;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.scene-label {
  pointer-events: none;
  white-space: nowrap;
  padding: 4px 8px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.82);
  color: #17251e;
  font-size: 12px;
  font-weight: 700;
}

@media (max-width: 1100px) {
  .app-shell {
    grid-template-columns: 240px minmax(0, 1fr);
  }

  .right-panel {
    grid-column: 1 / -1;
    border-left: 0;
    border-top: 1px solid #d7ded3;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
  }

  .detail-card {
    margin-bottom: 0;
  }
}

@media (max-width: 760px) {
  .app-shell {
    display: block;
  }

  .left-panel,
  .right-panel,
  .stage {
    min-height: auto;
  }

  .stage-header {
    display: grid;
  }

  .stage-header h2 {
    font-size: 23px;
  }

  .canvas-panel {
    height: 460px;
    min-height: 360px;
  }

  .timeline,
  .right-panel {
    grid-template-columns: 1fr;
  }
}'''


def verify_mjs() -> str:
    return r'''import { mkdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";
import { PNG } from "pngjs";

const url = process.env.APP_URL ?? "http://127.0.0.1:5173/";
const chromePath = process.env.CHROME_PATH ?? "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const outDir = new URL("../verification/", import.meta.url);

function outPath(fileName) {
  return fileURLToPath(new URL(fileName, outDir));
}

function assert(value, message) {
  if (!value) {
    throw new Error(message);
  }
}

async function visualMetrics(page, selector) {
  const buffer = await page.locator(selector).screenshot();
  const png = PNG.sync.read(buffer);
  let nonBackground = 0;
  let count = 0;

  for (let y = 0; y < png.height; y += 1) {
    for (let x = 0; x < png.width; x += 1) {
      const index = (png.width * y + x) * 4;
      const r = png.data[index];
      const g = png.data[index + 1];
      const b = png.data[index + 2];
      if (Math.abs(r - 238) + Math.abs(g - 243) + Math.abs(b - 238) > 36) {
        nonBackground += 1;
      }
      count += 1;
    }
  }

  return { nonBackgroundRatio: nonBackground / count, width: png.width, height: png.height };
}

async function verifyViewport(browser, name, viewport) {
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: "networkidle" });
  await page.waitForSelector("canvas", { timeout: 15000 });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: outPath(`${name}.png`), fullPage: true });
  await page.locator("canvas").screenshot({ path: outPath(`${name}-canvas.png`) });
  const metrics = await visualMetrics(page, "canvas");
  const title = await page.locator(".stage-header h2").innerText();
  assert(title.length > 0, `${name}: missing title`);
  assert(metrics.nonBackgroundRatio > 0.04, `${name}: canvas appears blank`);
  await page.close();
  return { name, title, metrics };
}

await mkdir(outDir, { recursive: true });

const browser = await chromium.launch({
  executablePath: chromePath,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});

try {
  const desktop = await verifyViewport(browser, "desktop", { width: 1440, height: 940 });
  const mobile = await verifyViewport(browser, "mobile", { width: 390, height: 900 });
  console.log(JSON.stringify({ ok: true, url, desktop, mobile }, null, 2));
} finally {
  await browser.close();
}'''


def generate(out_dir: Path, scene: dict[str, Any]) -> None:
    write_file(out_dir / "package.json", package_json())
    write_file(out_dir / "index.html", '<div id="root"></div><script type="module" src="/src/main.tsx"></script>')
    write_file(
        out_dir / "src" / "main.tsx",
        'import React from "react";\nimport ReactDOM from "react-dom/client";\nimport App from "./App";\n\nReactDOM.createRoot(document.getElementById("root")!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n);',
    )
    write_file(out_dir / "src" / "scene-data.ts", f"export const sceneData = {json.dumps(scene, indent=2, ensure_ascii=False)} as const;\nexport type SceneData = typeof sceneData;")
    write_file(out_dir / "src" / "App.tsx", app_tsx())
    write_file(out_dir / "src" / "styles.css", styles_css())
    write_file(out_dir / "src" / "vite-env.d.ts", '/// <reference types="vite/client" />')
    write_file(out_dir / "scripts" / "verify.mjs", verify_mjs())
    write_file(
        out_dir / "vite.config.ts",
        'import { defineConfig } from "vite";\nimport react from "@vitejs/plugin-react";\n\nexport default defineConfig({ plugins: [react()] });',
    )
    write_file(
        out_dir / "tsconfig.json",
        '{"files":[],"references":[{"path":"./tsconfig.app.json"},{"path":"./tsconfig.node.json"}]}',
    )
    write_file(
        out_dir / "tsconfig.app.json",
        '{"compilerOptions":{"tsBuildInfoFile":"./node_modules/.tmp/tsconfig.app.tsbuildinfo","target":"ES2022","useDefineForClassFields":true,"lib":["ES2022","DOM","DOM.Iterable"],"allowImportingTsExtensions":true,"verbatimModuleSyntax":true,"module":"ESNext","moduleResolution":"Bundler","noEmit":true,"jsx":"react-jsx","strict":true,"noUnusedLocals":true,"noUnusedParameters":true,"erasableSyntaxOnly":true,"noFallthroughCasesInSwitch":true,"noUncheckedSideEffectImports":true},"include":["src"]}',
    )
    write_file(
        out_dir / "tsconfig.node.json",
        '{"compilerOptions":{"tsBuildInfoFile":"./node_modules/.tmp/tsconfig.node.tsbuildinfo","target":"ES2023","lib":["ES2023"],"module":"ESNext","types":["node"],"skipLibCheck":true,"moduleResolution":"Bundler","allowImportingTsExtensions":true,"verbatimModuleSyntax":true,"moduleDetection":"force","noEmit":true,"strict":true,"noUnusedLocals":true,"noUnusedParameters":true,"erasableSyntaxOnly":true,"noFallthroughCasesInSwitch":true,"noUncheckedSideEffectImports":true},"include":["vite.config.ts"]}',
    )
    write_file(
        out_dir / "README.md",
        f"""# GeoMine Visualization Studio

Generated scene: {scene.get("title", "GeoMine scene")}

## Run

```bash
npm install
npm run dev
```

Open `http://127.0.0.1:5173/`.

## Verify

```bash
npm run build
npm run verify
```

This visualization is a research communication artifact. Conceptual geometry is not authoritative unless the scene data explicitly preserves verified geometry, CRS, scale, and source provenance.
""",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a GeoMine React/Vite/Three.js visualization page.")
    parser.add_argument("--output", required=True, help="Output directory for the generated Vite project.")
    parser.add_argument("--scene-data", help="Optional JSON SceneSpec. Defaults to a conceptual Athabasca uranium scene.")
    args = parser.parse_args()

    out_dir = Path(args.output).expanduser().resolve()
    scene_path = Path(args.scene_data).expanduser().resolve() if args.scene_data else None
    scene = load_scene(scene_path)
    generate(out_dir, scene)
    print(json.dumps({"ok": True, "output": str(out_dir), "title": scene.get("title")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
