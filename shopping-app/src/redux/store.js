import { createStore, applyMiddleware } from 'redux'
// import subscribersReducer from './subscribers/reducer'
import rootReducer from './rootReducer'
import logger from 'redux-logger'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension';


const middleware = [logger, thunk]
// const store = createStore(subscribersReducer)
const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(...middleware)))

export default store;