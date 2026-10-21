# Publish Hashimoire on GitHub Pages

The website uses **Docsify** and reads the same Markdown as the public GitHub repository. It does not require a domain, build server, or custom GitHub Actions workflow.

## First publication

1. Review and merge the active pull request containing `index.html`, `home.md`, `_sidebar.md`, `assets/site.css`, and `.nojekyll` into `main`.
2. In [repository Settings → Pages](https://github.com/mike-C-mike/hashimoire/settings/pages), choose **Deploy from a branch** under *Build and deployment → Source*.
3. Choose **main** as the branch and **/(root)** as the folder; click **Save**.
4. Wait for the Pages deployment to complete (check **Actions** or the Pages settings status).
5. Open **https://mike-C-mike.github.io/hashimoire/** and verify the homepage, search, navigation, Mermaid diagrams and mobile layout.

Do not choose `/docs`: the website `index.html` is in the repository root. Leave the **Custom domain** field blank.

## Maintenance

- Edit Markdown pages as usual; after changes land on `main`, GitHub Pages republishes.
- Add or remove links in `_sidebar.md` for the navigation menu.
- Edit `home.md` for homepage cards and `assets/site.css` for styling.
- Keep `.nojekyll` so GitHub Pages will serve files such as `_sidebar.md`.
- The page relies on JavaScript and external Docsify/Mermaid CDN assets; a browser or network that blocks those assets may show a loading message instead.

## Troubleshooting

- **404 at the URL:** check that the PR was merged and Pages points to `main /(root)`.
- **Site still says loading:** inspect the browser console and confirm CDN scripts are allowed.
- **A link fails:** use the sidebar's repository-root routes or relative Markdown paths validated from the source page.
- **Diagram remains code:** ensure Mermaid and the Docsify Mermaid plugin scripts load in the browser.
- **Old links containing `aquisition` fail:** update external bookmarks to `acquisition`; repository files have been renamed.

Official setup instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
