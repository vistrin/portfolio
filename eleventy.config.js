// Builds the static site from src/ into _site/. See CONTENT.md for how to edit content.
import fs from "node:fs";
import markdownIt from "markdown-it";
import { escape, renderExperience } from "./lib/experience.js";

const md = markdownIt({ html: true });
const readJson = (path) => JSON.parse(fs.readFileSync(path, "utf-8"));

export default function (eleventyConfig) {
  // data/ stays outside src/ because career-db exports straight into data/site.json.
  eleventyConfig.addWatchTarget("data/");
  eleventyConfig.addGlobalData("career", () => readJson("data/site.json"));
  eleventyConfig.addGlobalData("experienceLayout", () => readJson("data/experience_layout.json"));
  eleventyConfig.addGlobalData("buildDate", () =>
    new Date().toLocaleString("en-US", { month: "long", year: "numeric", timeZone: "UTC" }));

  eleventyConfig.addPassthroughCopy("src/style.css");
  eleventyConfig.addPassthroughCopy("src/site.js");

  // Case studies, in the order of their `num` field.
  eleventyConfig.addCollection("caseStudies", (api) =>
    api.getFilteredByGlob("src/case-studies/*.md").sort((a, b) => String(a.data.num).localeCompare(String(b.data.num))));

  // Text fields accept inline Markdown: *emphasis*, **bold**, [links](url). & and < are escaped for you.
  eleventyConfig.addFilter("md", (text) => md.renderInline(String(text ?? "")));
  // Same, flattened to plain text for use inside an attribute (meta descriptions).
  eleventyConfig.addFilter("attr", (text) => md.renderInline(String(text ?? "")).replace(/<[^>]*>/g, ""));
  eleventyConfig.addFilter("esc", escape);
  // Site links are relative ("devsecops.html", not "/devsecops.html") so the site works under any base path.
  eleventyConfig.addFilter("rel", (url) => (url === "/" ? "index.html" : url.replace(/^\//, "")));
  // The case study after this one; none after the last.
  eleventyConfig.addFilter("nextCase", (all, url) => all[all.findIndex((c) => c.url === url) + 1]);

  // {% diagram "edw.svg" %}: inlines src/_includes/diagrams/edw.svg, indented to sit inside the page.
  eleventyConfig.addShortcode("diagram", (file) =>
    fs.readFileSync(`src/_includes/diagrams/${file}`, "utf-8").replace(/\r\n/g, "\n").trimEnd()
      .split("\n").map((line, i) => (line && i ? "        " + line : line)).join("\n"));

  eleventyConfig.addShortcode("experience", renderExperience);
}

export const config = {
  dir: { input: "src", includes: "_includes", output: "_site" },
  markdownTemplateEngine: "liquid",
  htmlTemplateEngine: "liquid",
};
