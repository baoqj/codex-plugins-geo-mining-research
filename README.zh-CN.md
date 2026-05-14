# GeoMine Research

**语言：** [English](README.md) | 中文

GeoMine Research 是一个面向 Codex 的地球科学、地球化学、矿业研究和加拿大矿业信息工作流插件。它把 Codex skills、确定性脚本、可选 MCP server、数据来源/证据规则、测试和示例组织在同一个插件包中。

这个项目的基本原则是保守、可追溯、可复核：它可以帮助用户组织证据、设计研究流程、生成学术论文、构建模型包、生成图表和 PDF，但不会把自己包装成实时勘查数据库、Qualified Person 结论、法律意见、投资建议或已经验证的数值模拟器。

## 功能概览

GeoMine Research 支持：

- AOI 规范化、CRS 规划、加拿大优先的地学数据源发现。
- 地球化学调查解释和带 QA/QC 意识的证据综合。
- 矿点资料标准化和矿床模型匹配。
- NI 43-101 / CIM 术语风险审查。
- 学术论文架构设计、论文写作、公式/证据矩阵、同行评审式检查、数学公式安全的 PDF 导出。
- 学术 Figure Package：地图、地球化学图表、概念机制图、图注和可复现实作脚手架。
- 使用 React、Vite、Three.js 生成三维地质/GIS/矿化演示页面。
- PHREEQC Modeling Package：地下水化学、形态分布、饱和指数、水岩反应、反演建模计划和论文方法文字。
- THMC Modeling Skill Family：热-水-力-化学耦合地下水和反应运移研究设计。
- PFLOTRAN Modeling Skill Family：PFLOTRAN 输入文件、网格/材料、化学、运行、输出分析、校准验证和论文综合。
- 可选本地 MCP server，用于确定性工具合同、mock THMC 记录、DGR 现场数据采集和 PFLOTRAN 规划。

## 安全启动策略

默认情况下：

- `.codex-plugin/plugin.json` 不自动注册本地 skills。
- `.codex-plugin/plugin.json` 不自动注册 MCP servers。
- 插件根目录不带默认 `.mcp.json`。
- `references/*.mcp.example.json` 都是禁用状态的可选模板。

这样做是为了避免 Codex 启动时因为本地 Python、`uv`、MCP 依赖或路径不完整而失败。skills 和 MCP server 仍然保留在源码中，供显式安装和调试。

## 架构

```text
geo-mining-research/
  .codex-plugin/
    plugin.json
  docs/
    README.md
    GeoMine_Research_User_Manual.md
    GeoMine_Research_User_Manual.zh-CN.md
    PROJECT_ORGANIZATION_PLAN.md
  skills/
    geomine-research-router-skill/
    research-router-skill/
    academic-geochemistry-paper-architect/
    academic-paper-research-writer/
    figure-generation/academic-figure-package-skill/
    geomine-paper-pdf-export-skill/
    geomine-visualization-studio-skill/
    phreeqc-modeling-skill/
    thmc-modeling/
    pflotran-modeling/
    ...基础 GIS、地球化学、矿点、矿床、披露和综合 skill
  scripts/
    geomine_mcp_server.py
    geomine/
    run_mcp_sample_cases.py
    validate_plugin.py
  mcp/
    geomine-thmc-server/
  references/
    *.md
    *.mcp.example.json
  examples/
  tests/
```

核心工作流：

1. 理解用户问题并规范化实体。
2. 判断研究类型和证据通道。
3. 选择最小必要 skill 集合。
4. 只有在明确可用时才使用可选 MCP。
5. 保留 provenance、不确定性、限制条件和 caveats。
6. 输出 Markdown、模型包、Figure Package、可视化页面或 PDF。

## Skill 家族

| 领域 | 主要 skills | 用途 |
|---|---|---|
| 路由 | `geomine-research-router-skill`, `research-router-skill` | 实体规范化、任务分类、skill/MCP 选择和最终综合结构。 |
| 基础 GeoMine | `aoi-crs-normalizer-skill`, `geodata-discovery-skill`, `geochemical-survey-skill`, `mineral-occurrence-skill`, `deposit-model-skill`, `ni43-101-disclosure-check-skill`, `report-synthesis-skill` | AOI、GIS、地球化学、矿点、矿床模型、披露和报告基础。 |
| 学术写作 | `academic-geochemistry-paper-architect`, `academic-paper-research-writer`, `geomine-paper-pdf-export-skill` | 先设计论文架构，再写作，再导出 PDF。 |
| 图表与可视化 | `academic-figure-package-skill`, `geomine-visualization-studio-skill` | Figure Package、图注、GIS/地球化学图和 3D 概念场景。 |
| PHREEQC | `phreeqc-modeling-skill` | 地下水化学建模包和本地 PHREEQC 文件脚手架。 |
| THMC | `skills/thmc-modeling/` | 耦合等级、概念模型、控制方程、反应网络、求解器路线、验证、不确定性和 THMC 报告。 |
| PFLOTRAN | `skills/pflotran-modeling/` | 独立 PFLOTRAN Modeling Package、输入文件、网格/材料、化学、运行清单、输出分析和论文综合。 |

## MCP Servers

GeoMine 包含可选本地 MCP 实现：

| Server | 用途 | 默认状态 |
|---|---|---|
| `geomine` | AOI 规范化、加拿大公开数据源发现规划、provenance 总结、邻近矿权规划、基础设施距离规划。 | 禁用 |
| `geomine_thmc` | mock THMC 项目/AOI/水化学/岩性/矿物记录、PHREEQC draft/mock run、OGS/PFLOTRAN job、model version、run record。 | 禁用 |
| `geomine_thmc_data` | DGR 现场数据记录、钻孔、传感器、水样、岩芯、packer test、地应力、验证和数据包。 | 禁用 |
| `geomine_pflotran` | PFLOTRAN 输入文件、验证、run manifest、观测输出解析、结果总结和模型包。 | 禁用 |

mock 输出只说明工作流形态，不是已验证现场数据、求解器结果、安全评估或监管证据。

## 安装说明

本地 Codex 插件测试时，可以把目录复制或软链接到本地插件 marketplace，例如：

```text
~/.codex/plugins/geo-mining-research
```

然后在 Codex 插件界面或 CLI 中安装。除非需要本地 MCP 调试，否则应保持 MCP 禁用。

直接调试 MCP：

```bash
codex mcp add geomine \
  --env PYTHONPATH=/Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research/scripts \
  -- \
  uv \
  --directory /Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research \
  run \
  --no-project \
  --with \
  "mcp[cli]" \
  --with \
  httpx \
  python \
  scripts/geomine_mcp_server.py
```

更多内容见：

- [MCP_SETUP.md](MCP_SETUP.md)
- [THMC_MCP_INTEGRATION_GUIDE.md](THMC_MCP_INTEGRATION_GUIDE.md)
- [MCP_TROUBLESHOOTING.md](MCP_TROUBLESHOOTING.md)

## 示例 Prompt

```text
Use GeoMine Research to screen a Saskatchewan AOI for uranium potential using geology, geochemistry, mineral occurrences, and disclosure-safe caveats.
```

```text
Use GeoMine Research to design a geochemistry academic paper on uranium migration in fractured Canadian Shield groundwater using PHREEQC speciation and saturation indices.
```

```text
Use GeoMine Research THMC Modeling to build a THMC Modeling Package for tailings seepage, sulfide oxidation, shallow groundwater transport, and pH buffering.
```

```text
Use GeoMine Research to generate an Academic Figure Package for a uranium groundwater paper, including study-area map, Piper diagram, Eh-pH diagram, speciation plot, conceptual migration cross-section, captions, and publication checklist.
```

## 开发命令

```bash
python3 scripts/validate_plugin.py
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]>=1.2.0" --with "httpx>=0.28.0" python -m pytest
PYTHONPATH=scripts python3 scripts/run_mcp_sample_cases.py ../../report
python3 tests/validate_thmc_skill_family.py
python3 tests/validate_thmc_mcp_config.py
python3 scripts/test_thmc_mcp_tools.py
python3 scripts/test_thmc_data_mcp_tools.py
python3 scripts/test_pflotran_mcp_tools.py
uv --directory mcp/geomine-thmc-server run --with pytest python -m pytest
```

## 文档

- [docs/README.md](docs/README.md)
- [docs/GeoMine_Research_User_Manual.zh-CN.md](docs/GeoMine_Research_User_Manual.zh-CN.md)
- [docs/PROJECT_ORGANIZATION_PLAN.md](docs/PROJECT_ORGANIZATION_PLAN.md)

门户文档页面目标地址：

```text
https://openmine.vip/geomine/docs
```

## 项目改进迭代升级历史

### 0.1.0 - MVP Skill-only 插件

- 创建 GeoMine Research Codex 插件 MVP。
- 增加路由、AOI/CRS、数据源发现、地球化学调查、矿点、矿床模型、NI 43-101 风险检查和报告综合等基础 skills。
- 增加加拿大优先 references、entity schema、evidence matrix、examples、确定性脚本和测试。
- 建立安全边界：不提供法律意见、投资建议、Qualified Person 意见、可行性结论、资源/储量估算或许可决定。

### 0.2.0 - Deferred MCP 架构

- 增加本地 `geomine` MCP server entrypoint 和 pure tool layer。
- 增加 AOI 规范化、公开数据源发现规划、provenance、邻近矿权和基础设施距离规划等 10 个确定性 MCP tools。
- 把 MCP 激活移到 `references/` 下的禁用模板。
- 移除 manifest 中默认 `skills` 和 `mcpServers`，保证 Codex 启动安全。
- 增加 adapter/MCP 设计、source registry、CKAN/ArcGIS parser scaffold、MCP sample runner 和 smoke tests。

### 0.2.x - 学术研究与论文出版工作流

- 增加 `academic-paper-research-writer`，支持学术论文、假设、证据矩阵、公式 registry、引用纪律和 peer-review 检查。
- 增加 `geomine-paper-pdf-export-skill`，支持 Markdown 到 PDF，并正确处理数学、物理、化学符号和科学单位。
- 增加 `academic-geochemistry-paper-architect`，在写作前先判断地球化学论文类型，并控制论文架构、数据、方法、图表、引用、不确定性和结论边界。
- 增加 `academic-figure-package-skill`，支持论文图表包、图注、绘图 prompt、脚本 scaffold 和出版检查。

### 0.2.x - Visualization Studio

- 增加 `geomine-visualization-studio-skill`。
- 增加 uranium basin 和 research workflow 可视化 SceneSpec 示例。
- 支持使用 React/Vite/Three.js 生成概念地质、GIS、矿化、矿脉、钻孔和地质演化场景。

### 0.2.x - THMC Skill Family

- 增加 THMC Modeling Skill Family，覆盖 scenario routing、conceptual model、governing equations、hydro-transport、reaction network、thermal transport、mechanical damage/permeability、solver selection、validation、uncertainty、figure 和 synthesis。
- 增加 THMC Modeling Package 2.0 templates 和 schema。
- 增加可选 `geomine_thmc` MCP tools，用于 mock project context、水化学、岩性/矿物、mesh/parameter fields、PHREEQC draft/mock jobs、OGS/PFLOTRAN job lifecycle、model versions 和 run records。

### 0.2.x - DGR 现场数据和 PFLOTRAN 规划

- 增加 `dgr-field-data-acquisition-skill` 与 `geomine_thmc_data` MCP tools。
- 增加独立 `pflotran-modeling` skill family 和可选 `geomine_pflotran` planning MCP tools。
- 增加 PFLOTRAN input deck、grid/material、chemistry、THC、geomechanics、run-management、output-analysis、calibration/validation 和 paper-synthesis skills。

### 0.2.x - PHREEQC Modeling

- 增加独立 `phreeqc-modeling-skill`。
- 增加 references、templates、examples、本地脚本，用于水化学表检查、solution block、selected output、output parsing 和 run manifest。

### 当前整理与文档升级

- 将项目级文档收拢到 `docs/`。
- 增加英文/中文 README。
- 系统说明插件功能、架构、运行方式、能力边界、未完成工作和使用示例。
- 增加 OpenMine 门户 `/geomine/docs` 文档页面。

## 当前边界与后续工作

- Live source adapters 仍然保守，很多工具仍是 source planner、fixture parser 或 mock-backed workflow validator。
- PHREEQC、THMC 和 PFLOTRAN MCP 层目前重点是 package generation、draft inputs、mock runs、run records 和 planning。科学验证仍需要真实数据、真实求解器运行、校准和领域专家审查。
- 面向其他 Codex 用户的 marketplace 发布仍需最终打包策略、版本管理和安全审查。
- 公开技术披露输出必须由 Qualified Person 以及必要的法律/监管顾问审查。

## License

Proprietary。插件元信息见 `.codex-plugin/plugin.json`。
