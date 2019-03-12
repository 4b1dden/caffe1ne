import HomePage from './pages/home.vue';
import AboutPage from './pages/about.vue';
import FormPage from './pages/form.vue';
import DynamicRoutePage from './pages/dynamic-route.vue';
import NotFoundPage from './pages/not-found.vue';
import FullHistoryPage from './pages/full-history.vue';
import SettingsPage from './pages/settings.vue';

import PanelLeftPage from './pages/panel-left.vue';

export default [
  {
    path: '/',
    component: HomePage,
  },
  {
    path: '/panel-left/',
    component: PanelLeftPage,
  },
  {
    path: '/about/',
    component: AboutPage,
  },
  {
    path: '/form/',
    component: FormPage,
  },
  {
    path: '/dynamic-route/blog/:blogId/post/:postId/',
    component: DynamicRoutePage,
  },
  {
    path: '/full-history/',
    component: FullHistoryPage,
  },
  {
    path: '/settings/',
    component: SettingsPage
  },
  {
    path: '(.*)',
    component: NotFoundPage,
  },
];
