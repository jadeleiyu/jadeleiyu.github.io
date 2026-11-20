# Jade (Lei) Yu — personal website

日常只需要编辑根目录的两个文件，不需要修改前端代码。

| 想改什么 | 打开哪个文件 |
| --- | --- |
| 姓名、职位、单位、联系方式、简介、研究方向、经历 | [HOME.md](HOME.md) |
| 添加、删除、排序论文，修改作者、年份、链接 | [PUBLICATIONS.md](PUBLICATIONS.md) |
| 换头像 | 替换 `static/avatar.png` |
| 换 CV | 替换 `static/uploads/resume.pdf` |

## 日常更新

在 GitHub 仓库首页打开 `HOME.md` 或 `PUBLICATIONS.md`，点铅笔图标编辑，再点 **Commit changes**。
提交到 `main` 后，已有的 GitHub Actions 流程会构建和发布网站。可以在 **Actions → Publish website** 查看结果。
初次安装步骤见 [MIGRATION.md](MIGRATION.md)；完成后不需要在电脑上安装任何工具。

## 改简介

打开 `HOME.md`，找到 `## About`，直接修改下面的段落。文件开头的两条 `---` 之间是姓名、职位和链接；修改字段的文字即可。
如果字段中包含冒号，建议用英文双引号包住整段文字，例如 `role: "Research Scientist: LLMs"`。

## 加论文

打开 `PUBLICATIONS.md`，在对应年份下复制一条现有记录，再替换内容。无需创建文件夹，也无需 BibTeX 导入、生成 PR 或维护另一份数据。

```markdown
#### [Your paper title](https://example.org/paper)
**Lei Yu**, Author Two, Author Three
*Conference or journal* · 2026
[Code](https://example.org/code) · [Project](https://example.org/project)
```

链接可选。没有论文链接时，直接写 `#### Your paper title`。
新增年份时加一行 `### 2026`。论文按你在文件里的顺序显示；拖动或复制粘贴即可调整顺序。
`<!-- bibtex: ... -->` 是不可见的迁移标记，可保留或删除。

## 加 News、Projects 或其他板块

在 `HOME.md` 正文里添加二级标题和普通 Markdown：

```markdown
## News

- **November 2026:** Add your update here.
```

二级标题会自动加入顶部导航。标题建议使用简短的英文纯文本，且不要重复。
删除整个板块即可移除它；不需要修改导航配置。首页文字板块按文件顺序显示，论文列表单独显示在最后。

## 批量导入（可选）

当前的 23 条记录已经转换完成。平时直接编辑 `PUBLICATIONS.md` 最简单。
如果以后想一次导入很多条 BibTeX，可以使用可选转换脚本：

```sh
python -m pip install bibtexparser==1.4.3 pylatexenc==2.10
python scripts/bibtex_to_markdown.py your-papers.bib > imported.md
```

检查 `imported.md`，将需要的条目复制到 `PUBLICATIONS.md`。脚本只输出候选 Markdown，**不会覆盖任何网站内容**，也不参与发布。
不会自动查询论文元数据、猜测年份、补全不完整 arXiv ID 或合并不同版本。

## 实现

使用 Hugo 0.136.5 和本地模板，无外部主题、Node.js、数据库或浏览器 JavaScript 依赖。
`hugo.toml` 将根目录的两个 Markdown 文件映射到 Hugo 内容目录，生成到 `dist/`。
`layouts/` 和 `static/style.css` 只负责展示，日常无需打开。
如果要本地预览，安装 Hugo 后在项目目录运行 `hugo server`。

## 原始资料

`archive/original-publications.bib` 保留原始论文数据，仅作备份，不会自动覆盖网站。
`MIGRATION.md` 记录迁移范围和需要核对的项目。
