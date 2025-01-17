import { defineConfig } from 'vitepress'

//https://www.freecodecamp.org/news/how-to-build-a-modern-documentation-site-with-vitepress/

export default defineConfig({
  title: "GBIF Data Profiles",
  description: "A collection of interactive data profiles of GBIF occurrence datasets",
  themeConfig: {
    aside: false,
    layout: 'doc',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Profiles', link: '/dataset-profiles' }
    ],
    sidebar: [
      {
        text: 'Datasets',
        items: [
          { text: 'Interactive Profiles', link: '/dataset-profiles' },
          { text: 'Source Datasets', link: '/source-datasets' }
        ]
      }
    ]
  }
})
