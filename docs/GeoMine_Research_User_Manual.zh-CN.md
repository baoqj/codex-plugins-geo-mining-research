# GeoMine Research 使用手册

## 1. 项目概述

GeoMine Research 是一个面向 Codex 的研究型地球科学和矿业工作流插件。它适用于需要系统处理 AOI、地球化学数据、矿床模型、学术论文、图表、地下水化学、THMC 建模、PHREEQC、PFLOTRAN 和加拿大矿业披露边界的研究人员、分析人员和开发者。

它不是黑箱数据服务，而是一个面向 Codex 的结构化科研操作系统：

```text
问题 -> 实体规范化 -> 研究类型判断 -> skill 路由 -> 证据通道 -> 综合 -> artifact 生成
```

它把以下内容分开处理：

- 数据获取和 provenance；
- 地质解释和不确定性；
- 模型包设计；
- 学术写作；
- 图表、可视化和 PDF 导出；
- 监管和披露边界。

## 2. 设计原则

### 先证据，后结论

关键判断必须能追溯到数据集、来源、模型、公式、用户文件或显式 placeholder。插件不能编造 source id、化验值、样品数、地图图层、模型结果、DOI 或 live retrieval 结果。

### MCP 默认关闭

MCP server 作为本地实现和示例存在，但默认关闭。这样可以保证 Codex 启动稳定，也让 mock/live 状态保持明确。

### Skill 模块化

每个 skill 只负责一个明确任务。Router 选择最小必要 skill 集合，避免把所有工作塞进一个不可维护的大 prompt。

### 学术克制

GeoMine 可以帮助写科学论文，但不能夸大因果性、可行性、安全性、经济价值或监管结论。

### 可复现输出

输出应尽可能保留脚本、参数、来源版本、假设和生成 artifact，如 Markdown、PDF、JSON、图表或模型包文件。

## 3. 核心架构

GeoMine Research 包含五层：

1. 插件元数据和文档。
2. 用于推理、写作、建模、图表和综合的 skills。
3. references 和 templates。
4. 确定性 helper scripts。
5. 可选 MCP servers。

Router skills 是主要入口：

- `geomine-research-router-skill`
- `research-router-skill`

它们负责判断任务类型、规范化实体、选择 skill 通道，并保留输出边界。

## 4. 主要能力

### 4.1 基础 GeoMine Research

适用于 AOI screening、数据源规划、地球化学解释、矿点背景、矿床模型匹配和披露安全报告。

常用 skills：

- `aoi-crs-normalizer-skill`
- `geodata-discovery-skill`
- `geochemical-survey-skill`
- `mineral-occurrence-skill`
- `deposit-model-skill`
- `ni43-101-disclosure-check-skill`
- `report-synthesis-skill`

示例：

```text
Use GeoMine Research to screen a Saskatchewan AOI for uranium potential using public geology, geochemistry, mineral occurrence, and disclosure-safe caveats.
```

### 4.2 学术论文写作

适用于研究论文、期刊文章、正式报告、机制论文、公式推导、假设构建或同行评审式草稿。

核心流程：

```text
academic-geochemistry-paper-architect
  -> domain/model skills
  -> academic-paper-research-writer
  -> geomine-paper-pdf-export-skill
```

地球化学论文架构 skill 会先判断论文类型：

- Data Paper / Database Paper
- Regional Geochemical Characterization Paper
- Mineral Exploration Geochemistry Paper
- Petrogenesis Paper
- Isotope Geochemistry Paper
- Hydrogeochemistry Paper
- Environmental Geochemistry Paper
- Reactive Transport Modelling Paper
- Experimental Geochemistry Paper
- Radiolysis / Nuclear Geochemistry Paper
- Geochemical Modelling and Machine Learning Paper
- Review / Perspective Paper
- Technical Note / Methods Paper

示例：

```text
Use GeoMine Research to design and draft a hydrogeochemistry paper on uranium migration in fractured Canadian Shield groundwater using PHREEQC speciation and saturation indices.
```

### 4.3 Figure Package 与可视化

`academic-figure-package-skill` 用于出版级图表包设计，包括 figure inventory、visual grammar、captions、data/provenance requirements 和 reproducible script scaffolds。

`geomine-visualization-studio-skill` 用于 React/Vite/Three.js 概念场景，例如：

- 地质盆地边缘；
- 矿脉与断裂系统；
- 钻孔与地层；
- 科研流程；
- 地质演化动画。

示例：

```text
Use GeoMine Research to generate a 3D conceptual uranium basin-margin visualization page with stratigraphy, faults, drillholes, geochemical evidence lanes, provenance, and caveats.
```

### 4.4 PHREEQC Modeling

`phreeqc-modeling-skill` 用于独立地下水化学和地球化学反应模型设计。

支持：

- speciation；
- saturation index；
- batch reaction；
- equilibrium phases；
- kinetic reactions；
- surface complexation；
- ion exchange；
- gas phase；
- one-dimensional transport；
- inverse modeling；
- PhreeqcRM coupling plan。

它生成 PHREEQC Modeling Package、输入模板、selected output 设计、run manifest、methods text、missing-data list 和 uncertainty statement。它不会编造水化学数据、常数、矿物量或校准结果。

### 4.5 THMC Modeling

THMC family 支持热-水-力-化学耦合地下水和反应运移研究设计。

它可以设计：

- scenario classification；
- coupling level: H, HC, THC, HM, THM, THMC；
- conceptual model；
- governing equations；
- hydro-transport setup；
- geochemical reaction network；
- thermal transport；
- mechanical damage and porosity/permeability feedback；
- solver route；
- validation and sensitivity plan；
- THMC figures and report synthesis。

Core Mode 不需要 MCP。MCP-Enhanced Mode 可以在可用时使用 `geomine_thmc` 和 `geomine_thmc_data`。

### 4.6 PFLOTRAN Modeling

PFLOTRAN family 独立于 THMC，但可以接收 THMC conceptual outputs。

它支持：

- conceptual model；
- input deck skeleton；
- grid/material plan；
- flow and transport plan；
- chemistry and reaction plan；
- THC coupling plan；
- geomechanics boundary notes；
- run management；
- output/observation analysis；
- calibration/validation；
- paper synthesis。

可选 `geomine_pflotran` MCP server 是 planning layer，默认不执行 PFLOTRAN。

## 5. MCP 运行方式

GeoMine 有四个可选 MCP servers：

- `geomine`
- `geomine_thmc`
- `geomine_thmc_data`
- `geomine_pflotran`

配置模板：

- `references/geomine.mcp.example.json`
- `references/geomine-thmc.mcp.example.json`
- `references/geomine-thmc-data.mcp.example.json`
- `references/geomine-pflotran.mcp.example.json`

规则：

- 没有实际调用 MCP tool，就不能声称使用了 MCP。
- 不能把 mock output 写成 live evidence。
- 必须保留 `mode`、`provenance`、`warnings` 和 `errors`。
- secrets 不得写入日志或 prompt。

## 6. 安装和本地使用

可把插件复制或软链接到本地 Codex plugin marketplace，例如：

```text
~/.codex/plugins/geo-mining-research
```

然后通过 Codex 安装。如果需要 MCP，需要显式添加 MCP server。

验证命令：

```bash
python3 scripts/validate_plugin.py
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]>=1.2.0" --with "httpx>=0.28.0" python -m pytest
```

## 7. 使用案例

### AOI Screening

```text
Use GeoMine Research to screen the Athabasca Basin margin for uranium potential. Include geology, geochemistry, mineral occurrences, evidence gaps, and NI 43-101-safe caveats.
```

预期输出：

- normalized AOI and jurisdiction；
- evidence lanes；
- source plan；
- deposit-model fit；
- confidence and gaps；
- safe next-work recommendations。

### 学术地球化学论文

```text
Use GeoMine Research to write a geochemistry academic paper about carbonate-enhanced uranium migration in fractured groundwater. Use PHREEQC as the modeling method and export Markdown and PDF.
```

预期输出：

- paper type classification；
- research questions and hypotheses；
- data/method audit；
- PHREEQC package plan；
- evidence matrix；
- manuscript sections；
- formula-safe PDF export。

### THMC Modeling Package

```text
Use GeoMine Research THMC Modeling to build a THMC Modeling Package for sulfide tailings seepage, shallow groundwater transport, and pH buffering.
```

预期输出：

- scenario classification；
- active T/H/M/C processes；
- coupling level；
- governing equations；
- reaction network；
- solver route；
- validation/sensitivity plan；
- figure plan；
- modeling package。

### PFLOTRAN Modeling Package

```text
Use GeoMine Research to design a PFLOTRAN reactive transport model for uranium mobility in a 2D fractured aquifer.
```

预期输出：

- conceptual model；
- grid/material plan；
- flow/transport setup；
- chemistry blocks；
- input deck skeleton；
- output plan；
- run manifest；
- paper methods draft。

### Figure Package

```text
Use GeoMine Research to create a Figure Package for a uranium groundwater paper, including study area map, Piper diagram, Eh-pH diagram, saturation index plot, speciation plot, and conceptual migration cross-section.
```

预期输出：

- figure inventory；
- figure-by-figure specifications；
- axes, units, legends, source notes；
- script plans；
- captions；
- publication checklist。

## 8. 能力边界

GeoMine Research 不提供：

- 法律意见；
- 投资建议；
- Qualified Person 意见；
- 资源量或储量估算；
- 可行性结论；
- 许可决定；
- 已验证安全案例；
- live solver 保证；
- 自动验证的第三方数据集。

当数据缺失时，插件应使用 placeholder，并解释缺口如何影响解释。

## 9. 项目整理和路线图

当前整理策略：

- 保留已实现和测试覆盖的 skills 与 MCP layers；
- 继续保持 MCP default-off；
- 将项目级文档集中到 `docs/`；
- 清楚说明 mock/live 边界；
- 不删除仍被测试和文档引用的能力草稿；
- 完善公开文档和门户访问；
- 只有在确认可靠公开接口后，才把 source planner 升级成 bounded adapter。

见 [PROJECT_ORGANIZATION_PLAN.md](PROJECT_ORGANIZATION_PLAN.md)。
