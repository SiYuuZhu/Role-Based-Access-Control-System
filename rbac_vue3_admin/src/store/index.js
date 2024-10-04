import { createStore } from 'vuex'

export default createStore({
  state: {
    editableTabsValue: '/index',
    editableTabs:[
      {
        title: '首頁',
        name: '/index'
      }
    ]
  },
  getters: {
  },
  mutations: {
    // menu click
    ADD_TABS:(state, tab_child)=>{
      if(state.editableTabs.findIndex(e=>e.name === tab_child.path) === -1){
        state.editableTabs.push({
          title: tab_child.name,
          name: tab_child.path
        })
      }
      state.editableTabsValue = tab_child.path
    },
    // log out
    RESET_TAB:(state)=>{
      state.editableTabsValue='/index'
      state.editableTabs=[
        {
          title: '首頁',
          name: '/index'
        }
      ]
    }
  },
  actions: {
  },
  modules: {
  }
})
