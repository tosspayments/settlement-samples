class PaymentController < ApplicationController

  def settlements
    startDate = "2022-07-01"
	  endDate = "2022-07-29"
	  page = 1
	  size = 100
         
    search = "?startDate=#{startDate}&endDate=#{endDate}&page=#{page}&size=#{size}"
      
    options = {
      headers: {
        Authorization: "Basic " + Base64.strict_encode64("test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y:"),
        "Content-Type": "application/json"
      }
    }
      
	  begin
      response = HTTParty.get("https://api.tosspayments.com/v1/settlements" + search, options).parsed_response
      @Response = response
    end
      
  end 
  
end