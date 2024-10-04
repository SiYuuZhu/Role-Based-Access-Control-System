import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import SvgIcon from '@/icons'
import 'element-plus/dist/index.css'
import zhTW from 'element-plus/es/locale/lang/zh-tw'
import '@/assets/styles/border.css'
import '@/assets/styles/reset.css'

createApp(App).use(store).use(router).use(ElementPlus).mount('#app')



const app=createApp(App)
SvgIcon(app);

app.use(store)
app.use(router)
app.use(ElementPlus, {
    locale: zhTW,
  })
app.mount('#app')