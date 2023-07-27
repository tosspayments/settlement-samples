Rails.application.routes.draw do
    # add code
  
    get 'apis/settlements' => 'apis#settlements'
    
    # end code
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
