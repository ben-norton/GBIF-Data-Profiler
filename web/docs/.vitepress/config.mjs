import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "GBIF Dataset Profiles",
  description: "The purpose of this website to provide access to a collection of data profiles and supporting analytics of GBIF occurrence datasets. The profiles themselves are generated with a series of python libraries.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    aside: false,
    layout: 'doc',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' },
    ],

    sidebar: [
      {
        text: 'Specifications',
        items: [
          { text: 'Dataset Inventory', link: '/source-data-inventory' },
          { text: 'Dataset Corrections', link: '/dataset-corrections'}
        ]
      }
    ]
  }
})
