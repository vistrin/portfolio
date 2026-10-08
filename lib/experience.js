// Renders the Experience page body from data/site.json (exported from career-db)
// and data/experience_layout.json (which entries appear, in which groups).
// Ported from the old build.py; output is identical.

export function escape(text) {
  // Element text and double-quoted attributes; leaves apostrophes readable.
  return String(text).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function fail(msg) {
  throw new Error(`experience: ${msg}`);
}

function linkedinLink(profile) {
  const handle = profile.linkedin;
  return `<a href="https://www.${escape(handle)}" target="_blank" rel="noopener">${escape(handle)}</a>`;
}

export function renderExperience(site, layout) {
  const p = site.profile;
  const employers = Object.fromEntries(site.employers.map((e) => [e.id, e]));
  const entries = Object.fromEntries(site.entries.map((e) => [e.id, e]));
  const summary = site.summary || fail("site.json has no summary; set site_export.summary in career-db");
  const out = [];
  const w = (line) => out.push(line);

  w('      <div class="cs-header">');
  w('        <div class="cs-num">Experience</div>');
  w(`        <h1 class="cs-title" id="resume-title">${escape(summary.headline)}</h1>`);
  w(`        <div class="cs-sub"><a href="mailto:${escape(p.email)}">${escape(p.email)}</a> · ${linkedinLink(p)}</div>`);
  w('      </div>');
  w('');
  w(`      <p class="resume-summary">${escape(summary.text)}</p>`);

  const blocks = site.skill_blocks || [];
  if (blocks.length) {
    const multi = blocks.length > 1;
    w('');
    w('      <div class="resume-block">');
    w('        <h2 class="section-label">Skills</h2>');
    if (multi) w('        <div class="skills-cols">');
    for (const b of blocks) {
      const label = escape(b.category);
      if (multi) w(`          <div>\n            <h3 class="cs-col-label">${label}</h3>`);
      w(`        <ul class="card-tags" aria-label="${label}">`);
      for (const item of b.items) w(`          <li class="tag">${escape(item)}</li>`);
      w('        </ul>');
      if (multi) w('          </div>');
    }
    if (multi) w('        </div>');
    w('      </div>');
  }

  w('');
  w('      <div class="resume-block">');
  w('        <h2 class="section-label">Professional experience</h2>');
  for (const job of layout.jobs) {
    const emp = employers[job.employer] || fail(`layout employer ${job.employer} has no approved entries in site.json`);
    const org = "org" in job ? job.org : emp.name;
    const meta = [emp.location, emp.dates].filter(Boolean).join(" · ");
    w('');
    w('        <article class="job">');
    w('          <header class="job-head">');
    if (org) {
      w('            <div>');
      w(`              <h3 class="job-title">${escape(emp.title)}</h3>`);
      w(`              <p class="job-org">${escape(org)}</p>`);
      w('            </div>');
    } else {
      w(`            <h3 class="job-title">${escape(emp.title)}</h3>`);
    }
    w(`            <p class="job-meta">${escape(meta)}</p>`);
    w('          </header>');
    for (const group of job.groups) {
      if (group.heading) {
        let text = escape(group.heading);
        if (group.link) text = `<a href="${escape(group.link)}">${text}</a>`;
        w('');
        w(`          <h4 class="job-group">${text}</h4>`);
      }
      w('          <ul class="resume-list">');
      for (const i of group.entries) {
        const e = entries[i] || fail(`layout entry ${i} is not an approved resume entry in site.json`);
        if (e.employer_id !== job.employer) fail(`layout entry ${i} belongs to ${e.employer_id}, not ${job.employer}`);
        w(`            <li data-entry="${escape(i)}">${escape(e.text)}</li>`);
      }
      w('          </ul>');
    }
    w('        </article>');
  }
  w('      </div>');

  w('');
  w('      <div class="resume-block">');
  w('        <h2 class="section-label">Education</h2>');
  w('        <ul class="edu-list">');
  for (const ed of site.education) w(`          <li><strong>${escape(ed.degree)}</strong><span>${escape(ed.school)}</span></li>`);
  w('        </ul>');
  w('      </div>');

  if (site.publications && site.publications.length) {
    w('');
    w('      <div class="resume-block">');
    w('        <h2 class="section-label">Publications</h2>');
    for (const pub of site.publications) w(`        <p class="pub">${escape(pub.citation)}</p>`);
    w('      </div>');
  }
  return out.join("\n");
}
