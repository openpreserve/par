package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@ApiModel(description = "A list of business rules")
public class BusinessRules {

    @SerializedName("businessRules")
    private List<BusinessRule> businessRules = null;

    public void addBusinessRule(BusinessRule businessRule) {
        if (this.businessRules == null) {
            this.businessRules = new ArrayList<>();
        }
        this.businessRules.add(businessRule);
    }

    /**
     * Get businessRules
     *
     * @return businessRules
     **/
    @ApiModelProperty(value = "")
    public List<BusinessRule> getBusinessRules() {
        if (this.businessRules == null) {
            this.businessRules = new ArrayList<>();
        }
        return businessRules;
    }

    public void setBusinessRules(List<BusinessRule> businessRules) {
        this.businessRules = businessRules;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        BusinessRules businessRules = (BusinessRules) o;
        return Objects.equals(this.businessRules, businessRules.getBusinessRules());
    }

    @Override
    public int hashCode() {
        return Objects.hash(businessRules);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class BusinessRules {\n");

        sb.append("    businessRules: ").append(toIndentedString(businessRules)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
